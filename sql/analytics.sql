-- Total claims per patient
SELECT 
    patient_first_name,
    patient_last_name,
    SUM(amount) AS total_claim_amount
FROM CLAIMS_GOLD
GROUP BY patient_first_name, patient_last_name;

-- Daily claims trend
SELECT 
    service_date,
    COUNT(*) AS total_claims,
    SUM(amount) AS total_amount
FROM CLAIMS_GOLD
GROUP BY service_date
ORDER BY service_date;

-- Top providers
SELECT 
    provider_id,
    COUNT(*) AS total_claims,
    SUM(amount) AS total_amount
FROM CLAIMS_GOLD
GROUP BY provider_id
ORDER BY total_amount DESC
LIMIT 10;

-- Data quality validation
SELECT *
FROM CLAIMS_SILVER
WHERE claim_id IS NULL
OR amount <= 0
OR service_date IS NULL;