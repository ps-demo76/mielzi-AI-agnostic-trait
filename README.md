# mielzi-AI-agnostic-trait - The Whole Shebang

**Para kay daughter - simple explanation**

### Ano ba ito?
Isang 12-step na pag-iisip na pipeline. Parang utak na may checklist.

### Paano gumagana? (How it works)
1. **Steps 1-3 - Perception**: Intindihin ang tanong
   - Step 1: Ano ang sinabi?
   - Step 2: Ano ang context?
   - Step 3: Ano ang gusto talaga?

2. **Steps 4-6 - Reasoning**: Mag-isip
   - Step 4: Gumawa ng hula
   - Step 5: Maghanap ng ebidensya
   - Step 6: Pagsamahin

3. **Steps 7-8 - Red Team**: Hanapan ng mali (falsification)
   - Step 7: Ano ang pwedeng mali?
   - Step 8: Ayusin

4. **Step 9 - Reconciliation - Meta AI Runner**
   - Ito ang `agents/meta_ai_runner.py`
   - Powered by Meta AI (Muse Spark 1.1) - Meta's model
   - Open-weight reference: Muse Glimmer
   - Chine-check niya kung tama ang format gamit ang `schema/pipeline.schema.json`
   - Output: "Unified: ..."

5. **Steps 10-12 - Final Output**
   - Step 10: Final sagot
   - Step 11: Gaano ka-confident?
   - Step 12: Ipaliwanag sa bata

### Anong laman ng bawat file?
- `schema/pipeline.schema.json` - rules ng bawat step
- `agents/meta_ai_runner.py` - Step 9, nagva-validate
- `pipeline.py / main.py` - buong 12 steps demo
- `traits/example_trait.json` - halimbawa ng trait para sa bata
- `requirements.txt` - `jsonschema` lang kailangan

### Paano patakbuhin?
```bash
pip install -r requirements.txt
python main.py
# or
python pipeline.py
```

Makikita mo ang 12 steps na naka-JSON.

### GitHub URL
`github.com/ps-demo76/ps-demo76` -> folder `mielzi-AI-agnostic-trait`

I-drag lang lahat ng files dito sa GitHub upload box tapos Commit changes.

### Para sa anak mo - laruin niya:
Palitan niya ang `user_question` sa `main.py`:
```python
result = run_pipeline("Bakit asul ang langit?")
```

Tapos run ulit.
