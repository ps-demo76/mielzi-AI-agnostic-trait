# mielzi-AI-agnostic-trait

12-step reasoning pipeline with red-team falsification.

## Structure
- `schema/pipeline.schema.json` - JSON schema for pipeline steps
- `agents/meta_ai_runner.py` - Meta AI runner for reconciliation (step 9)

## Runner
Meta AI powered by Muse Spark 1.1 from Meta.
Open-weight reference: Muse Glimmer.

## Test
pip install jsonschema
python -m agents.meta_ai_runner
