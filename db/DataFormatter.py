class DataFormatter:
    def format(self, raw_data):
        # raw data in the form : {"country1":[f1, f2, ...], "country2": [f1, f2, ...], ...}
        # we want [{"country":country, "f1": f1, "f2": f2, ...}, {...}, ...]
        labels = raw_data["labels"]
        del raw_data["labels"]
        data = []
        for country, features in raw_data.items():
            features_dict = {}
            for label, feature in zip(labels, features):
                print(label)
                features_dict[label] = self.formatFeature(feature)
            features_dict["country"] = country
            data += [features_dict]

        print(data)
        return data

    def formatFeature(self, raw):
        if raw:
            if raw == "-" or raw == "N/A":
                return None
            else:
                formatted = raw.replace(',', '').replace('%', '')
                if ' ' in formatted:
                    firstSpace = formatted.index(' ')
                    formatted = formatted[:firstSpace]
                return float(formatted)
        else:
            return None
