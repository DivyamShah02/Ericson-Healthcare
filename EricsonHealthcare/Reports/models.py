from django.db import models

# Create your models here.


from django.db import models

class PADeathReport(models.Model):
    claim_number = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    insured_name = models.CharField(max_length=200)
    claimant_name = models.CharField(max_length=200)
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=200)
    policy_type = models.CharField(max_length=200)
    channel_sourcing = models.TextField(null=True, blank=True)
    
    # Observation Details
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField()
    claimant_visit = models.TextField()
    
    # Hospital Visit Details
    other_insurance = models.CharField(max_length=200, null=True, blank=True)
    mlc_done = models.CharField(max_length=200, null=True, blank=True)
    fir_collected = models.BooleanField(default=False)
    pm_report_details = models.TextField(null=True, blank=True)
    casuality_note = models.TextField(null=True, blank=True)
    
    # Police Visit Details
    fir_details = models.TextField(null=True, blank=True)
    pm_center_name = models.CharField(max_length=200, null=True, blank=True)
    
    # Spot Visit Details
    photos_done = models.BooleanField(default=False)
    witnesses = models.CharField(max_length=200, null=True, blank=True)
    total_person_inquired = models.IntegerField(null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    
    # Media Coverage
    media_provided = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion_details = models.TextField()
    report_closed_date = models.DateField(null=True, blank=True)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim Report - {self.claim_number}"
    

class TTDReport(models.Model):
    claim_number = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    insured_name = models.CharField(max_length=200)
    claimant_name = models.CharField(max_length=200)
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=200)
    policy_type = models.CharField(max_length=200)
    channel_sourcing = models.TextField(null=True, blank=True)

    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField()
    claimant_visit = models.TextField()
    current_condition_disablity_case = models.CharField(max_length=200, null=True, blank=True)
    other_insurance = models.CharField(max_length=200, null=True, blank=True)

    mlc = models.CharField(max_length=200, null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)
    date_of_discharge = models.DateField(null=True, blank=True)
    post_mortem = models.CharField(max_length=200, null=True, blank=True)

    
    hospital_visit_details = models.TextField()
    
    # PM Center Visit
    police_verification_details = models.TextField()
    police_final_report = models.TextField()
    case_summary = models.TextField()
    police_document_verified = models.TextField()
    cause_of_death =  models.CharField(max_length=200, null=True, blank=True)
    viscera_status = models.CharField(max_length=200, null=True, blank=True)
    pm_verified =  models.CharField(max_length=200, null=True, blank=True)

    # Spot Visit
    spot_visit_photos = models.CharField(max_length=200, null=True, blank=True)
    spot_visit_witness = models.CharField(max_length=200, null=True, blank=True)
    spot_visit_description = models.CharField(max_length=200, null=True, blank=True)

    # dl verification
    dl_name = models.CharField(max_length=200, null=True, blank=True)
    dl_validity = models.CharField(max_length=200, null=True, blank=True)
    cov = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    # rc verification
    owner_name = models.CharField(max_length=200, null=True, blank=True)
    registration_validity = models.DateField(null=True, blank=True)
    vehicle_details = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    # vicinity check
    total_person_inquired = models.IntegerField(null=True, blank=True)
    event_details = models.CharField(max_length=200, null=True, blank=True)

    # industry feedback
    other_insurance_company = models.CharField(max_length=200, null=True, blank=True)
    claim_status = models.CharField(max_length=200, null=True, blank=True)

    conclusion = models.TextField()
    intimation_date = models.DateField(null=True, blank=True)
    report_closed_date = models.DateField(null=True, blank=True)
    tat = models.IntegerField(null=True, blank=True)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)

    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TTD Report - {self.claim_number}"

class HealthClaimReport(models.Model): # RR GR
    # insured details
    insurer = models.CharField(max_length=200, null=True, blank=True)
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    present_policy_number = models.CharField(max_length=200, null=True, blank=True)
    policy_start_date = models.DateField(null=True, blank=True)
    policy_end_date = models.DateField(null=True, blank=True)
    claim_number = models.CharField(max_length=200, null=True, blank=True)
    claim_amount = models.CharField(max_length=200, null=True, blank=True)

    # hospital details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_sex = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)
    date_of_discharge = models.DateField(null=True, blank=True)
    address_and_witness_name = models.CharField(max_length=200, null=True, blank=True)
    ipd_no = models.CharField(max_length=200, null=True, blank=True)
    room_category = models.CharField(max_length=200, null=True, blank=True)
    present_complaint_with_duration = models.CharField(max_length=200, null=True, blank=True)
    medical_history_with_duration = models.CharField(max_length=200, null=True, blank=True)
    any_previous_history_of_similar_complaints = models.CharField(max_length=200, null=True, blank=True)
    diagnosis = models.CharField(max_length=200, null=True, blank=True)
    family_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_registration_number = models.CharField(max_length=200, null=True, blank=True)

    # accident related claims
    date_and_time_of_accident = models.DateTimeField(null=True, blank=True)
    detailed_narration_of_how_accident_happended = models.TextField(null=True, blank=True)
    is_insured_holding_any_pa_with_us_or_others = models.CharField(max_length=200, null=True, blank=True)
    fir_mlc_done = models.BooleanField(null=True, blank=True)
    scar_mark_verification = models.CharField(max_length=200, null=True, blank=True)
    any_alcoholism_factor_noted = models.CharField(max_length=200, null=True, blank=True)
    INCIDENT_TYPE_CHOICES = [
        ('accident', 'Accident'),
        ('assault', 'Assault'),
        ('suicidal_attempt', 'Suicidal Attempt'),
    ]
    incident_type = models.CharField(
        max_length=20,
        choices=INCIDENT_TYPE_CHOICES,
        default='accident',  # Default selection
    )
    whether_stay_justified_or_prologned_with_nature = models.CharField(max_length=200, null=True, blank=True)
    attending_doctors_opinion_on_cause_of_injury_and_alcoholism = models.CharField(max_length=100, 
                                                                                   null=True,blank=True
                                                                                   )
    any_previous_history_of_similar_complaints = models.IntegerField(null=True, blank=True)
    # Brief description of the Case covering Findings of the Investigator, 
    # Details of past Claims of same Insured, whatever applicable. 
    # Findings of the Claims Processing

    brief_findings = models.TextField(null=True, blank=True)

    # Hospital Visit Details
    total_beds = models.IntegerField(null=True, blank=True)
    operation_theatre = models.CharField(max_length=200, null=True, blank=True)
    no_of_rms = models.IntegerField(null=True, blank=True)
    no_of_doctors = models.IntegerField(null=True, blank=True)
    no_of_nurses = models.IntegerField(null=True, blank=True)

    hospital_registration_number = models.IntegerField(null=True, blank=True)
    validity = models.DateField(null=True, blank=True)
    hospital_tariff_card = models.CharField(max_length=200, null=True, blank=True)
    hospital_visit_findings = models.TextField(null=True, blank=True)


    discharge_summary_icp_and_treating_doctor_statement = models.CharField(max_length=200, null=True, blank=True)
    opd_paper_date = models.DateField(null=True, blank=True)
    opd_details = models.TextField(null=True, blank=True)
    
    ipd_register_details = models.TextField(null=True, blank=True)
    hospital_statement = models.TextField(null=True, blank=True)
    pharmacy_visit_details = models.TextField(null=True, blank=True)
    pharmacy_statement = models.TextField(null=True, blank=True)
    pathology_statement = models.TextField(null=True, blank=True)
    resident_visit_findings = models.TextField(null=True, blank=True)
    home_visit = models.TextField(null=True, blank=True)
    insured_statement = models.TextField(null=True, blank=True)
    lab_name = models.TextField(null=True, blank=True)
    lap_reports = models.TextField(null=True, blank=True)
    complete_blood_count = models.TextField(null=True, blank=True)
    pharmacy_name = models.CharField(max_length=200, null=True, blank=True)
    employment_visit = models.TextField(null=True, blank=True)
    vicinity_check = models.CharField(max_length=200, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    evidences = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Health Claim Report - {self.claim_number}"
