from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Pis-py/m2m100_AYI_TEKK_wo_fr_40")

model = AutoModelForSeq2SeqLM.from_pretrained("Pis-py/m2m100_AYI_TEKK_wo_fr_40")

#r = "sama bopp dey metti"


def traduction(r):
    model_inputs = tokenizer(r, return_tensors="pt")
    # translate to French
    gen_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id("fr"))
    return tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)