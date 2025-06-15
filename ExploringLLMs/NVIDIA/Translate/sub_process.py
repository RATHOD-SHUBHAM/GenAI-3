import subprocess
import os

HOME = os.getcwd()
# print(HOME)

class Translate:
    def __init__(self, api_key):
        self.api_key = api_key

    def translate_text(self, text, source_lang='en', target_lang='de'):
        try:
            command = [
                'python', f'{HOME}/python-clients/scripts/nmt/nmt.py',
                '--server', 'grpc.nvcf.nvidia.com:443', '--use-ssl',
                '--metadata', 'function-id', '647147c1-9c23-496c-8304-2e29e7574510',
                '--metadata', 'authorization', f'Bearer {self.api_key}',
                '--text', text,
                '--source-language-code', source_lang,
                '--target-language-code', target_lang
            ]

            result = subprocess.run(command, check=True, capture_output=True, text=True)
            # print(result)
            # print(type(result.stdout))
            print("Translation Output:\n", result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error during translation:", e.stderr)
        except FileNotFoundError:
            print("Error: The specified script or command was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_supported_models(self):
        try:
            command = [
                'python', f'{HOME}/python-clients/scripts/nmt/nmt.py',
                '--server', 'grpc.nvcf.nvidia.com:443', '--use-ssl',
                '--metadata', 'function-id', '647147c1-9c23-496c-8304-2e29e7574510',
                '--metadata', 'authorization', f'Bearer {self.api_key}',
                '--list-models'
            ]

            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("Supported Models:\n", result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error while listing models:", e.stderr)
        except FileNotFoundError:
            print("Error: The specified script or command was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    obj = Translate(api_key="")
    # List all the available language
    # obj.list_supported_models()

    # Translate the language
    text = "Hi, how are you?"
    source_lang = 'en'
    target_lang = 'es' # SPanish
    obj.translate_text(text=text, source_lang=source_lang, target_lang=target_lang)

