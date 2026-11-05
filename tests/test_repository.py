"""Lightweight standard-library checks (no restricted audio or DSP packages needed)."""
from pathlib import Path
import json, subprocess, sys, unittest

ROOT=Path(__file__).resolve().parents[1]
NB=ROOT/'notebooks'/'FastICA_Audio_Source_Separation.ipynb'

class RepositorySafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notebook=json.loads(NB.read_text(encoding='utf-8'))
        cls.code='\n'.join(''.join(c['source']) for c in cls.notebook['cells'] if c['cell_type']=='code')

    def test_notebook_has_no_saved_media(self):
        self.assertTrue(all(not c.get('outputs') and c.get('execution_count') is None for c in self.notebook['cells'] if c['cell_type']=='code'))

    def test_every_cell_compiles(self):
        for i,c in enumerate(self.notebook['cells']):
            if c['cell_type']=='code':
                compile(''.join(c['source']),f'cell{i}','exec')

    def test_three_profiles_and_methods(self):
        for marker in ('original', 'custom', 'demo', 'run_fastica', 'run_pca', 'run_nmf', 'evaluate_and_align', 'bss_eval_sources'):
            self.assertIn(marker,self.code)

    def test_privacy_and_metadata(self):
        self.assertIn('ENABLE_INLINE_AUDIO_PLAYBACK = True',self.code)
        self.assertIn('SAVE_PRIVATE_AUDIO_FILES = False',self.code)
        self.assertIn('SHOW_PRIVATE_SIGNAL_FIGURES = False',self.code)
        self.assertIn('"input_basenames"',self.code)
        self.assertNotIn('"file_paths": FILE_PATHS',self.code)

    def test_required_project_files(self):
        for name in ('LICENSE','README.md','CITATION.cff','CITATION.bib','AUTHORS.md','REPRODUCIBILITY.md','DATA_AVAILABILITY.md','METHODS_AND_LIMITATIONS.md','CONTRIBUTING.md','SECURITY.md','CODE_OF_CONDUCT.md','requirements.txt','.gitignore'):
            self.assertTrue((ROOT/name).is_file(),name)

    def test_release_checker(self):
        r=subprocess.run([sys.executable,str(ROOT/'scripts'/'check_public_release.py')],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)

if __name__=='__main__':
    unittest.main()
