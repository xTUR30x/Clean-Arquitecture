#Adapter Pattern

class XLMDataProcessor:
    def process_data(self, xml_data):
        print(f"Procesando datos XML: { xml_data }")

class JsonDataProcessor:
    def process_json_data(self, json_data):
        print(f"Procesando datos JSON: { json_data }")

class JsonToXMLAdapter:
    def __init__(self, json_procesor: JsonDataProcessor) -> None:
        self.json_processor = json_procesor

    def process_data(self, xml_data):
        # Convertir XML a JSON
        json_data = f"{{'data': '{xml_data}'}}"
        self.json_processor.process_json_data(json_data)


if __name__ == '__main__':
    xml_processor = XLMDataProcessor()
    json_processor = JsonDataProcessor()
    adapter = JsonToXMLAdapter(json_processor)

    adapter.process_data("<data>Ejemplo</data>")
