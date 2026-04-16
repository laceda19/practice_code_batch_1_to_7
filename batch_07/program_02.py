text_input = input("Enter text: ")
suffix = input("Enter suffix to remove: ")
if text_input.endswith(suffix):
    result_text = text_input[:-len(suffix)]
else:
    result_text = text_input
print("Result:", result_text)