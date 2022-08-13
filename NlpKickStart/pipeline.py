from typing import List


class Pipeline:
    def __init__(self, components: List) -> None:
        self.components = components

    def __call__(self, texts: List[str]) -> List[str]:
        outputs = []
        for text in texts:
            output = text
            for component in self.components:
                output = component(output)
            outputs.append(output)
        return outputs
