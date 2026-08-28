import json
from jsonschema import validate

class MetaAIRunner:
    def __init__(self, schema_path="schema/pipeline.schema.json"):
        with open(schema_path) as f:
            self.schema = json.load(f)

    def reconcile(self, out):
        validate(instance=out, schema=self.schema)
        return {
            "step": 9,
            "agent": "Meta AI",
            "role": "Reconciliation",
            "input": json.dumps(out),
            "output": "Unified: " + out["output"],
            "confidence": 0.88
        }
