from agents.meta_ai_runner import MetaAIRunner
import json

def run_pipeline(user_question: str):
    steps = []
    
    # 1-3 Perception
    steps.append({"step":1,"agent":"Perception","role":"Input Parse","input":user_question,"output":f"Question understood: {user_question}","confidence":0.95})
    steps.append({"step":2,"agent":"Perception","role":"Context","input":user_question,"output":"Gather context","confidence":0.9})
    steps.append({"step":3,"agent":"Perception","role":"Intent","input":user_question,"output":"Intent: explain how it works","confidence":0.92})
    
    # 4-6 Reasoning
    steps.append({"step":4,"agent":"Reasoner","role":"Hypothesis","input":user_question,"output":"Hypothesis: user wants full flow","confidence":0.85})
    steps.append({"step":5,"agent":"Reasoner","role":"Evidence","input":user_question,"output":"Evidence: files exist in repo","confidence":0.8})
    steps.append({"step":6,"agent":"Reasoner","role":"Synthesis","input":user_question,"output":"Synthesis ready","confidence":0.82})
    
    # 7-8 Red Team (falsification)
    steps.append({"step":7,"agent":"RedTeam","role":"Counter-argument","input":user_question,"output":"Check: is output too vague?","confidence":0.75})
    steps.append({"step":8,"agent":"RedTeam","role":"Fix","input":user_question,"output":"Fix: make it specific and kid-friendly","confidence":0.78})
    
    # 9 Reconciliation - Meta AI
    runner = MetaAIRunner()
    reconciled = runner.reconcile(steps[-1])
    steps.append(reconciled)
    
    # 10-12 Output
    steps.append({"step":10,"agent":"Writer","role":"Final Answer","input":user_question,"output":reconciled["output"] + " -> Ready for GitHub","confidence":reconciled["confidence"]})
    steps.append({"step":11,"agent":"Writer","role":"Confidence Check","input":user_question,"output":f"Confidence {reconciled['confidence']}","confidence":reconciled["confidence"]})
    steps.append({"step":12,"agent":"Writer","role":"Explain","input":user_question,"output":"Explained in README for daughter","confidence":0.9})
    
    return steps

if __name__ == "__main__":
    result = run_pipeline("how does it work?")
    print(json.dumps(result, indent=2))
