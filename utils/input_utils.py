class InputUtils:
    def int_input(prompt: str, min: int = None, max: int = None, default: int = None) -> int:
        try:
            input_text = input(prompt)

            if not input_text:
                if default:
                    return default

                return InputUtils.int_input(prompt, default)

            value = int(input_text)

            if min is not None and value <= min:
                print(f"Value is too small. Min value is {min} Lets try again...")
                return InputUtils.int_input(prompt, min, max, default)

            if max is not None and value >= max:
                print(f"Value is too big. Max value is {max} Lets try again...")
                return InputUtils.int_input(prompt, min, max, default)

            return int(input_text)
        except:
            print("Somthing went wrong. Lets try again...")
            return InputUtils.int_input(prompt, default)

    def str_input(prompt: str, default: str = None) -> str:
        try:
            input_text = input(prompt)

            if not input_text:
                if default:
                    return default

                return InputUtils.str_input(prompt, default)

            return input_text
        except:
            print("Somthing went wrong. Lets try again...")
            return InputUtils.str_input(prompt, default)
