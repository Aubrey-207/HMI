class QssTool:
    @staticmethod
    def setQssToObj(file_name, obj):
        with open(file_name, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)