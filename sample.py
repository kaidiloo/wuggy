# from wuggy import WuggyGenerator

# from my_custom_plugin.orthographic_estonian import BaseLanguagePlugin

# g = WuggyGenerator()
# g.load("orthographic_estonian", BaseLanguagePlugin())
# for w in g.generate_classic(["jõgi"]):
#     print(w)

from wuggy import WuggyGenerator
from csv import DictWriter

from orthographic_estonian.orthographic_estonian import OfficialLanguagePlugin

g = WuggyGenerator()
g.load("orthographic_estonian", OfficialLanguagePlugin())

pseudoword_matches = g.generate_classic(["jõgi"])
g.export_classic_pseudoword_matches_to_csv(pseudoword_matches, "./pseudowords.csv")
# for w in g.generate_classic(["jõgi"]):
#     print(w["pseudoword"])
#     # print(w)

# from wuggy import WuggyGenerator

# g = WuggyGenerator()
# g.load("orthographic_english")
# for w in g.generate_classic(["target"]):
#     print(w)