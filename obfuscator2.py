import ast
import random
def yamam(original_code):
    class Obfuscator(ast.NodeTransformer):
        def __init__(self):
            self.names_map = {}

        def obfuscate_name(self, name):
            # Simple renaming scheme, can be made more complex
            if name not in self.names_map:
                obfuscated_name = f"var_{random.randint(1000, 9999)}"
                self.names_map[name] = obfuscated_name
            return self.names_map[name]

        def visit_FunctionDef(self, node):
            node.name = self.obfuscate_name(node.name)
            self.generic_visit(node)
            return node

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):
                node.id = self.obfuscate_name(node.id)
            return node

    def obfuscate_code(source_code):
        tree = ast.parse(source_code)
        obfuscator = Obfuscator()
        obfuscated_tree = obfuscator.visit(tree)
        obfuscated_code = ast.unparse(obfuscated_tree)
        return obfuscated_code

    # Example usage



