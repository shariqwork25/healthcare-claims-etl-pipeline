def parse_edi_837(file_path):

    claims = []
    claim = {}

    with open(file_path, "r") as f:
        segments = f.read().split("~")

    for seg in segments:

        elements = seg.split("*")

        if elements[0] == "CLM":
            claim["claim_id"] = elements[1]
            claim["amount"] = float(elements[2])

        elif elements[0] == "NM1" and elements[1] == "QC":
            claim["patient_last_name"] = elements[3]
            claim["patient_first_name"] = elements[4]

        elif elements[0] == "DTP":
            claim["service_date"] = elements[3]

        elif elements[0] == "NM1" and elements[1] == "85":
            claim["provider_id"] = elements[-1]

        elif elements[0] == "SE":
            claims.append(claim)
            claim = {}

    return claims