# Contributing

Contributions are welcome for clarity, portability, tests, documentation and reproducibility, subject to appropriate intellectual-property rights and participant privacy.

1. Open a GitHub Issue describing a bug, compatibility concern, or proposed method extension. For private security issues follow [`SECURITY.md`](SECURITY.md).
2. Make changes in a separate branch. Keep any changes to the original paper's experiment settings clearly separated from new experiments and state whether metrics are directly comparable.
3. Use **synthetic/permissioned recordings** for examples and tests. Do **not** submit participant voices, derived mixtures, playback outputs, real speaker names, private local paths or personally identifying information. Do not upload original HTML exports containing embedded media.
4. Before creating a PR: `python scripts/check_public_release.py`; `python -m unittest discover -s tests -v`; check the notebook has zero outputs and execution counters.
5. Document Python/library compatibility, the run profile and exact preprocessing needed to reproduce any newly reported scores. Do not rewrite or silently remove the legacy `mir_eval` evaluator.
6. By submitting code, you represent that you have the right to contribute it under the repository's MIT license. Do not submit copied proprietary code or recordings.

Contact the maintainer at [razuahmed038@gmail.com](mailto:razuahmed038@gmail.com) for questions about collaborations or research reuse. For access to original restricted data, follow the journal article's Data Availability Statement, not GitHub issues.