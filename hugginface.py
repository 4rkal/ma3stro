from gradio_client import Client

client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				"jazz",	# str  in 'Describe your music' Textbox component
				"output.wav",	# str (filepath or URL to file) in 'File' Audio component
				fn_index=0
)
print(result)