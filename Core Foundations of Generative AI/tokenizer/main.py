import tiktoken

def tokenizer(user_txt):
  # Encoding the tokens:
  enc = tiktoken.encoding_for_model("gpt-4o")
  encoded_tokens = enc.encode(user_txt)
  print("Encoded Tokens:", encoded_tokens)

  # Decoding the tokens:
  decoded_tokens = enc.decode([80685, 14987, 67, 2090])
  print("Decoded tokens:", decoded_tokens)


user_text = input("User: ")
tokenizer(user_text)
