from django.db import models

class PADeathReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID
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
    case_id = models.IntegerField()  # Link to Case ID
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


class HealthClaimReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID # RR GR
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


class CashlessClaimReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID
    claim_number = models.CharField(max_length=100, null=True, blank=True)
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    ilhc_trigger = models.CharField(max_length=200, null=True, blank=True)
    date_of_visit = models.DateField(null=True, blank=True)
    date_of_intimation = models.DateField(null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)
    pt_admitted = models.DateField(null=True, blank=True)
    advance_paid_details = models.CharField(max_length=100, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    ipd_details_finding = models.TextField(null=True, blank=True)
    insured_statement = models.TextField(null=True, blank=True)
    treating_dr_statement = models.TextField(null=True, blank=True)
    home_visit_if_plan_admission = models.CharField(max_length=100, null=True, blank=True)
    other_findings = models.TextField(null=True, blank=True)
    evidences_attached_uploaded_in_ft = models.BooleanField(null=True, blank=True)
    final_recommendation = models.TextField(null=True, blank=True)


class ClaimReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID # PPD
    claim_number = models.CharField(max_length=50)
    policy_number = models.CharField(max_length=50)
    insured_name = models.CharField(max_length=100)
    claimant_name = models.CharField(max_length=100)
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=100)
    channel_sourcing = models.CharField(max_length=200, null=True, blank=True)
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=50)
    insured_occupation = models.CharField(max_length=200)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField()
    hospital_visit_details = models.TextField()
    current_condition = models.CharField(max_length=200)
    other_insurance = models.TextField(null=True, blank=True)
    mlc_done = models.BooleanField(default=False)
    post_mortem_done = models.BooleanField(default=False)
    casuality_note = models.TextField(null=True, blank=True)
    hospital_visit_details = models.TextField(null=True, blank=True)
    verification_details = models.CharField(max_length=200, null=True, blank=True)
    final_report = models.TextField(null=True, blank=True)
    case_summary = models.TextField(null=True, blank=True)
    police_document_verified = models.CharField(max_length=200, null=True, blank=True)
    pm_centre_name = models.CharField(max_length=200, null=True, blank=True)
    cause_of_death = models.CharField(max_length=200, null=True, blank=True)
    viscera_status = models.CharField(max_length=200, null=True, blank=True)
    pm_verified = models.BooleanField(default=False)

    photos = models.CharField(max_length=200, null=True, blank=True)
    witness = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True) 

    dl_name = models.CharField(max_length=200, null=True, blank=True)
    dl_validity = models.DateField(null=True, blank=True)
    cov = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    total_person_inquired = models.IntegerField(null=True, blank=True)
    vicinity_check_details = models.TextField(null=True, blank=True)

    media_date = models.DateField(null=True, blank=True)
    media_details = models.TextField(null=True, blank=True)

    other_insurance_company = models.CharField(max_length=200, null=True, blank=True)
    claim_status = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)

    intimation_date = models.DateField()
    report_closed_date = models.DateField()
    turn_around_time = models.IntegerField()
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Claim Report - {self.claim_number}"
    

class HDCClosureReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    nol = models.CharField(max_length=50, null=True, blank=True)  # Nature of Loss
    policy_details = models.TextField(null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    hospital_name = models.CharField(max_length=100, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)  # Date of Journey
    doa = models.DateField(null=True, blank=True)  # Date of Admission
    dod = models.DateField(null=True, blank=True)  # Date of Discharge
    diagnosis = models.TextField(null=True, blank=True)
    trigger = models.TextField(null=True, blank=True)
    date_of_allocation = models.DateField(null=True, blank=True)
    date_of_closure = models.DateField(null=True, blank=True)
    closure_tat = models.IntegerField(null=True, blank=True)  # Turnaround Time in days
    case_introduction = models.TextField(null=True, blank=True)
    insured_part_details = models.TextField(null=True, blank=True)
    hospital_part_details = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)
    discrepancy_findings = models.TextField(null=True, blank=True)
    recommendation = models.TextField(null=True, blank=True)
    ground_of_rejection = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"HDC Closure Report - {self.claim_no or 'Unknown'}"


class ICLMClosureReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID # LOJ
    # Insured Information
    insured_name = models.CharField(max_length=255)
    policy_no = models.CharField(max_length=50)
    claim_no = models.CharField(max_length=50)
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2)
    policy_inception = models.DateField(null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    # Recommendation
    iclm_recommendation = models.CharField(max_length=50, default="Payable")

    # Insured Visit Details
    insured_details = models.TextField()
    insured_address = models.TextField()
    insured_mobile = models.CharField(max_length=15)
    insured_statement = models.TextField(blank=True, null=True)

    # Employment Details
    employer_name = models.CharField(max_length=255)
    employer_address = models.TextField()
    designation = models.CharField(max_length=255)
    nature_of_joining = models.CharField(max_length=255)
    employment_period = models.CharField(max_length=255)

    # PF Details
    pf_details = models.TextField(null=True, blank=True)

    # Bank Account Details
    bank_statement_downloaded_on = models.DateField(null=True, blank=True)
    last_salary_credited_on = models.DateField(null=True, blank=True)

    # Reason for Loss of Job
    reason_for_loss_of_job = models.TextField(blank=True, null=True)

    # Conclusion
    conclusion = models.TextField()

    # Intimation and Closure Dates
    date_of_intimation = models.DateField(null=True, blank=True)
    date_of_closure = models.DateField(null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.IntegerField(null=True, blank=True)
    state_manager_name = models.CharField(max_length=255)
    central_manager_name = models.CharField(max_length=255)

    def __str__(self):
        return f"ICLM Closure Report - {self.claim_no}"


class SecureMindCriticalIllnessReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID    #SMC
    # Insured Information
    insured_name = models.CharField(max_length=255)
    policy_no = models.CharField(max_length=50)
    claim_no = models.CharField(max_length=50)
    sum_insured = models.DecimalField(max_digits=12, decimal_places=2)
    policy_inception = models.DateField(null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    # Recommendation
    iclm_recommendation = models.CharField(max_length=50, choices=[("Repudiate", "Repudiate"), ("Payable", "Payable"), ("Query", "Query")])

    # Insured Visit Details
    insured_age_sex = models.CharField(max_length=50)
    insured_address = models.TextField()
    insured_mobile = models.CharField(max_length=15)

    # CI Event Details
    ci_event_narration = models.TextField(blank=True, null=True)
    past_history_treatment = models.TextField(blank=True, null=True)
    ci_details = models.TextField(blank=True, null=True)

    # Employment Details
    employer_name = models.CharField(max_length=255)
    employer_address = models.TextField()
    ghi_policy = models.CharField(max_length=255, blank=True, null=True)
    industry_check = models.CharField(max_length=255, blank=True, null=True)
    medical_leave_details = models.TextField(blank=True, null=True)

    # Other Insurance Policy
    other_policy_details = models.TextField(blank=True, null=True)
    ucv = models.CharField(max_length=255, blank=True, null=True)

    # Treating Doctor Visit
    treating_doctor_name = models.CharField(max_length=255)
    treating_doctor_designation = models.CharField(max_length=255)
    treating_doctor_registration = models.CharField(max_length=50, blank=True, null=True)
    treating_hospital_name = models.CharField(max_length=255)

    detailed_narration_of_ci_event = models.CharField(max_length=255)
    details_of_past_history = models.CharField(max_length=255)
    details_of_ci = models.CharField(max_length=255)

    doctor_details = models.TextField()

    # Hospitalization Details
    first_hospital_name = models.CharField(max_length=255)
    first_hospital_city = models.CharField(max_length=255)
    first_doa = models.DateField(null=True, blank=True)
    first_dod = models.DateField(null=True, blank=True)
    first_diagnosis = models.TextField(blank=True, null=True)
    first_icp_findings = models.TextField(blank=True, null=True)
    second_hospital_name = models.CharField(max_length=255, blank=True, null=True)
    second_doa = models.DateField(null=True, blank=True)
    second_dod = models.DateField(null=True, blank=True)
    second_diagnosis = models.TextField(blank=True, null=True)
    second_icp_findings = models.TextField(blank=True, null=True)

    #OPD Details
    opd_details = models.TextField(blank=True, null=True)

    # Investigation Details
    investigation_done = models.TextField(blank=True, null=True)

    # Conclusion
    conclusion = models.TextField(blank=True, null=True)

    # Intimation and Closure Dates
    date_of_intimation = models.DateField(null=True, blank=True)
    date_of_closure = models.DateField(null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.IntegerField(null=True, blank=True)
    state_manager_name = models.CharField(max_length=255)
    investigator_name = models.CharField(max_length=255)
    central_manager_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Critical Illness Report - {self.claim_no}"

