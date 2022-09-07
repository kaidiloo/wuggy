from wuggy import WuggyGenerator

from my_custom_plugin.orthographic_estonian import LanguagePlugin

g = WuggyGenerator()
g.load("orthographic_estonian", LanguagePlugin())
for w in g.generate_classic(["jõgi"]):
    print(w)
