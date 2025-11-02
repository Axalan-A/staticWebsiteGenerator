class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        if self.props is not None:
            for key in self.props:
                string += f"{key}=\"{self.props[key]}\" "

    def __repr__(self):
        return f"""
        Type: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}
        """
        
