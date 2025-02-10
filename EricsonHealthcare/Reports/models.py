from django.db import models

#PA Death
class PADeathReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
    claim_number = models.CharField(max_length=100, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    claimant_name = models.CharField(max_length=200, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=200, null=True, blank=True)
    policy_type = models.CharField(max_length=200, null=True, blank=True)
    channel_sourcing = models.TextField(null=True, blank=True)
    
    # Observation Details
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    claimant_visit = models.TextField(null=True, blank=True)
    
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
    total_person_inquired = models.CharField(max_length=255, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    
    # Media Coverage
    media_provided = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion_details = models.TextField(null=True, blank=True)
    intimation_date = models.TextField(null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time (TAT)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)
    
    # Investigator & Management Details
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim Report - {self.claim_number}"

#TTD
class TTDReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
    claim_number = models.CharField(max_length=100, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    claimant_name = models.CharField(max_length=200, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=200, null=True, blank=True)
    policy_type = models.CharField(max_length=200, null=True, blank=True)
    channel_sourcing = models.TextField(null=True, blank=True)

    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    claimant_visit = models.TextField(null=True, blank=True)
    current_condition_disablity_case = models.CharField(max_length=200, null=True, blank=True)
    other_insurance = models.CharField(max_length=200, null=True, blank=True)

    mlc = models.CharField(max_length=200, null=True, blank=True)
    date_of_admission = models.CharField(max_length=200, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=200, null=True, blank=True)
    post_mortem = models.CharField(max_length=200, null=True, blank=True)

    hospital_visit_details = models.TextField(null=True, blank=True)
    
    # PM Center Visit
    police_verification_details = models.TextField(null=True, blank=True)
    police_final_report = models.TextField(null=True, blank=True)
    case_summary = models.TextField(null=True, blank=True)
    police_document_verified = models.TextField(null=True, blank=True)
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
    registration_validity = models.CharField(max_length=200, null=True, blank=True)
    vehicle_details = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    # vicinity check
    total_person_inquired = models.CharField(max_length=255, null=True, blank=True)
    event_details = models.CharField(max_length=200, null=True, blank=True)

    # industry feedback
    other_insurance_company = models.CharField(max_length=200, null=True, blank=True)
    claim_status = models.CharField(max_length=200, null=True, blank=True)

    conclusion = models.TextField(null=True, blank=True)
    intimation_date = models.CharField(max_length=200, null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)

    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TTD Report - {self.claim_number}"


# class HealthClaimReport(models.Model):
#     case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # RR GR
#     # insured details
#     insurer = models.CharField(max_length=200, null=True, blank=True)
#     insured_name = models.CharField(max_length=200, null=True, blank=True)
#     contact_number = models.CharField(max_length=10, null=True, blank=True)
#     present_policy_number = models.CharField(max_length=200, null=True, blank=True)
#     policy_start_date = models.CharField(max_length=200, null=True, blank=True)
#     policy_end_date = models.CharField(max_length=200, null=True, blank=True)
#     claim_number = models.CharField(max_length=200, null=True, blank=True)
#     claim_amount = models.CharField(max_length=200, null=True, blank=True)

#     # hospital details
#     patient_name = models.CharField(max_length=200, null=True, blank=True)
#     patient_age = models.CharField(max_length=255, null=True, blank=True)
#     patient_sex = models.CharField(max_length=200, null=True, blank=True)
#     relation_with_insured = models.CharField(max_length=200, null=True, blank=True)
#     date_of_admission = models.CharField(max_length=200, null=True, blank=True)
#     date_of_discharge = models.CharField(max_length=200, null=True, blank=True)
#     address_and_witness_name = models.CharField(max_length=200, null=True, blank=True)
#     ipd_no = models.CharField(max_length=200, null=True, blank=True)
#     room_category = models.CharField(max_length=200, null=True, blank=True)
#     present_complaint_with_duration = models.CharField(max_length=200, null=True, blank=True)
#     medical_history_with_duration = models.CharField(max_length=200, null=True, blank=True)
#     any_previous_history_of_similar_complaints = models.CharField(max_length=200, null=True, blank=True)
#     diagnosis = models.CharField(max_length=200, null=True, blank=True)
#     family_doctor_name = models.CharField(max_length=200, null=True, blank=True)
#     treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
#     treating_doctor_registration_number = models.CharField(max_length=200, null=True, blank=True)

#     # accident related claims
#     date_and_time_of_accident = models.CharField(max_length=255, null=True, blank=True)
#     detailed_narration_of_how_accident_happended = models.TextField(null=True, blank=True)
#     is_insured_holding_any_pa_with_us_or_others = models.CharField(max_length=200, null=True, blank=True)
#     fir_mlc_done = models.BooleanField()
#     scar_mark_verification = models.CharField(max_length=200, null=True, blank=True)
#     any_alcoholism_factor_noted = models.CharField(max_length=200, null=True, blank=True)
#     INCIDENT_TYPE_CHOICES = [
#         ('accident', 'Accident'),
#         ('assault', 'Assault'),
#         ('suicidal_attempt', 'Suicidal Attempt'),
#     ]
#     incident_type = models.CharField(
#         max_length=20, null=True, blank=True,
#       ,
#         default='accident',  # Default selection
#     )
#     whether_stay_justified_or_prologned_with_nature = models.CharField(max_length=200, null=True, blank=True)
#     attending_doctors_opinion_on_cause_of_injury_and_alcoholism = models.CharField(max_length=100,, null=True, blank=True 
#                                                                                    
#                                                                                    )
#     any_previous_history_of_similar_complaints = models.CharField(max_length=255, null=True, blank=True)
#     # Brief description of the Case covering Findings of the Investigator, 
#     # Details of past Claims of same Insured, whatever applicable. 
#     # Findings of the Claims Processing

#     brief_findings = models.TextField(null=True, blank=True)

#     # Hospital Visit Details
#     total_beds = models.CharField(max_length=255, null=True, blank=True)
#     operation_theatre = models.CharField(max_length=200, null=True, blank=True)
#     no_of_rms = models.CharField(max_length=255, null=True, blank=True)
#     no_of_doctors = models.CharField(max_length=255, null=True, blank=True)
#     no_of_nurses = models.CharField(max_length=255, null=True, blank=True)

#     hospital_registration_number = models.CharField(max_length=255, null=True, blank=True)
#     validity = models.CharField(max_length=200, null=True, blank=True)
#     hospital_tariff_card = models.CharField(max_length=200, null=True, blank=True)
#     hospital_visit_findings = models.TextField(null=True, blank=True)


#     discharge_summary_icp_and_treating_doctor_statement = models.CharField(max_length=200, null=True, blank=True)
#     opd_paper_date = models.CharField(max_length=200, null=True, blank=True)
#     opd_details = models.TextField(null=True, blank=True)
    
#     ipd_register_details = models.TextField(null=True, blank=True)
#     hospital_statement = models.TextField(null=True, blank=True)
#     pharmacy_visit_details = models.TextField(null=True, blank=True)
#     pharmacy_statement = models.TextField(null=True, blank=True)
#     pathology_statement = models.TextField(null=True, blank=True)
#     resident_visit_findings = models.TextField(null=True, blank=True)
#     home_visit = models.TextField(null=True, blank=True)
#     insured_statement = models.TextField(null=True, blank=True)
#     lab_name = models.TextField(null=True, blank=True)
#     lap_reports = models.TextField(null=True, blank=True)
#     complete_blood_count = models.TextField(null=True, blank=True)
#     pharmacy_name = models.CharField(max_length=200, null=True, blank=True)
#     employment_visit = models.TextField(null=True, blank=True)
#     vicinity_check = models.CharField(max_length=200, null=True, blank=True)
#     conclusion = models.TextField(null=True, blank=True)
#     evidences = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"Health Claim Report - {self.claim_number}"


# class CashlessClaimReport(models.Model):
#     case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
#     claim_number = models.CharField(max_length=100, null=True, blank=True)
#     hospital_name = models.CharField(max_length=200, null=True, blank=True)
#     date_of_joining = models.CharField(max_length=200, null=True, blank=True)
#     ilhc_trigger = models.CharField(max_length=200, null=True, blank=True)
#     date_of_visit = models.CharField(max_length=200, null=True, blank=True)
#     date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
#     date_of_admission = models.CharField(max_length=200, null=True, blank=True)
#     pt_admitted = models.CharField(max_length=200, null=True, blank=True)
#     advance_paid_details = models.CharField(max_length=100, null=True, blank=True)
#     room_category = models.CharField(max_length=100, null=True, blank=True)
#     ipd_details_finding = models.TextField(null=True, blank=True)
#     insured_statement = models.TextField(null=True, blank=True)
#     treating_dr_statement = models.TextField(null=True, blank=True)
#     home_visit_if_plan_admission = models.CharField(max_length=100, null=True, blank=True)
#     other_findings = models.TextField(null=True, blank=True)
#     evidences_attached_uploaded_in_ft = models.BooleanField()
#     final_recommendation = models.TextField(null=True, blank=True)

#PPD
class PermanentPartialDisabilityFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # PPD
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    claimant_name = models.CharField(max_length=100, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)
    channel_sourcing = models.CharField(max_length=200, null=True, blank=True)
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=50, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    hospital_visit_details = models.TextField(null=True, blank=True)
    current_condition = models.CharField(max_length=200, null=True, blank=True)
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
    dl_validity = models.CharField(max_length=200, null=True, blank=True)
    cov = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    total_person_inquired = models.CharField(max_length=255, null=True, blank=True)
    vicinity_check_details = models.TextField(null=True, blank=True)

    media_date = models.CharField(max_length=200, null=True, blank=True)
    media_details = models.TextField(null=True, blank=True)

    other_insurance_company = models.CharField(max_length=200, null=True, blank=True)
    claim_status = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)

    intimation_date = models.CharField(max_length=200, null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    turn_around_time = models.CharField(max_length=255, null=True, blank=True)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Claim Report - {self.claim_number}"
    
#PA HDC
class PersonalAccidentHDCFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    nol = models.CharField(max_length=50, null=True, blank=True)  # Nature of Loss
    policy_details = models.TextField(null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    hospital_name = models.CharField(max_length=100, null=True, blank=True)
    doj = models.CharField(max_length=200, null=True, blank=True)  # Date of Journe, null=True, blank=Truey
    doa = models.CharField(max_length=200, null=True, blank=True)  # Date of Admissio, null=True, blank=Truen
    dod = models.CharField(max_length=200, null=True, blank=True)  # Date of Discharg, null=True, blank=Truee
    diagnosis = models.TextField(null=True, blank=True)
    trigger = models.TextField(null=True, blank=True)
    date_of_allocation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)
    closure_tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time in days
    case_introduction = models.TextField(null=True, blank=True)
    insured_part_details = models.TextField(null=True, blank=True)
    hospital_part_details = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)
    discrepancy_findings = models.TextField(null=True, blank=True)
    recommendation = models.TextField(null=True, blank=True)
    
    final_conclusion = models.TextField(null=True, blank=True)

    intimation_date = models.TextField(null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time (TAT)
    final_recommendation = models.CharField(max_length=200, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"HDC Closure Report - {self.claim_no or 'Unknown'}"

#LOJ
class LossOfJobFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # LOJ
    # Insured Information
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    policy_inception = models.CharField(max_length=200, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    # Recommendation
    iclm_recommendation = models.CharField(max_length=50, null=True, blank=True)

    # Insured Visit Details
    insured_details = models.TextField(null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)
    insured_mobile = models.CharField(max_length=15, null=True, blank=True)
    insured_statement = models.TextField(null=True, blank=True)

    # Employment Details
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    nature_of_joining = models.CharField(max_length=255, null=True, blank=True)
    employment_period = models.CharField(max_length=255, null=True, blank=True)

    # PF Details
    pf_details = models.TextField(null=True, blank=True)

    # Bank Account Details
    bank_statement_downloaded_on = models.CharField(max_length=100, null=True, blank=True)
    last_salary_credited_on = models.CharField(max_length=100, null=True, blank=True)

    # Reason for Loss of Job
    reason_for_loss_of_job = models.TextField(null=True, blank=True)

    # Conclusion
    conclusion = models.TextField(null=True, blank=True)

    # Intimation and Closure Dates
    date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=255, null=True, blank=True)
    central_manager_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"LoJ Closure Report - {self.claim_no}"

#SMCritical Illness Final
class SecureMindCriticalIllnessFinalReport(models.Model):

    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID    #SMC
    # Insured Information
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    policy_inception = models.CharField(max_length=200, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    # Recommendation
    iclm_recommendation = models.TextField(null=True, blank=True)

    # Insured Visit Details
    insured_details = models.CharField(max_length=200, null=True, blank=True)
    insured_age_sex = models.CharField(max_length=50, null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)
    insured_mobile = models.CharField(max_length=15, null=True, blank=True)

    # CI Event Details
    ci_event_narration = models.TextField(null=True, blank=True)
    past_history_treatment = models.TextField(null=True, blank=True)
    ci_details = models.TextField(null=True, blank=True)

    # Employment Details
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    ghi_policy = models.CharField(max_length=255, null=True, blank=True)
    industry_check = models.CharField(max_length=255, null=True, blank=True)
    medical_leave_details = models.TextField(null=True, blank=True)

    # Other Insurance Policy
    other_policy_details = models.TextField(null=True, blank=True)
    ucv = models.CharField(max_length=255, null=True, blank=True)

    # Treating Doctor Visit
    treating_doctor_details = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_designation = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_registration = models.CharField(max_length=50, null=True, blank=True)
    treating_hospital_name = models.CharField(max_length=255, null=True, blank=True)

    detailed_narration_of_ci_event = models.CharField(max_length=255, null=True, blank=True)
    details_of_past_history = models.CharField(max_length=255, null=True, blank=True)
    details_of_ci = models.CharField(max_length=255, null=True, blank=True)

    doctor_details = models.TextField(null=True, blank=True)

    # Hospitalization Details
    first_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    first_hospital_city = models.CharField(max_length=255, null=True, blank=True)
    first_doa = models.CharField(max_length=200, null=True, blank=True)
    first_dod = models.CharField(max_length=200, null=True, blank=True)
    first_diagnosis = models.TextField(null=True, blank=True)
    first_icp_findings = models.TextField(null=True, blank=True)
    second_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    second_doa = models.CharField(max_length=200, null=True, blank=True)
    second_dod = models.CharField(max_length=200, null=True, blank=True)
    second_diagnosis = models.TextField(null=True, blank=True)
    second_icp_findings = models.TextField(null=True, blank=True)

    #OPD Details
    opd_details = models.TextField(null=True, blank=True)

    # Investigation Details
    investigation_done = models.TextField(null=True, blank=True)

    # Conclusion
    conclusion = models.TextField(null=True, blank=True)

    # Intimation and Closure Dates
    date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=255, null=True, blank=True)
    investigator_name = models.CharField(max_length=255, null=True, blank=True)
    central_manager_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Secure Mind Illness Final Report - {self.claim_no}"

#SMC_Death
class SecureMindCriticalIllnessDeathFinalReport(models.Model):

    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID    #SMC
    # Insured Information
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    policy_inception = models.CharField(max_length=200, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    # Recommendation
    iclm_recommendation = models.TextField(null=True, blank=True)

    # Insured Visit Details
    insured_details = models.CharField(max_length=200, null=True, blank=True)
    insured_age_sex = models.CharField(max_length=50, null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)
    insured_mobile = models.CharField(max_length=15, null=True, blank=True)

    # CI Event Details
    ci_event_narration = models.TextField(null=True, blank=True)
    past_history_treatment = models.TextField(null=True, blank=True)
    ci_details = models.TextField(null=True, blank=True)

    # Employment Details
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    ghi_policy = models.CharField(max_length=255, null=True, blank=True)
    industry_check = models.CharField(max_length=255, null=True, blank=True)
    medical_leave_details = models.TextField(null=True, blank=True)

    # Other Insurance Policy
    other_policy_details = models.TextField(null=True, blank=True)
    ucv = models.CharField(max_length=255, null=True, blank=True)

    # Treating Doctor Visit
    treating_doctor_details = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_designation = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_registration = models.CharField(max_length=50, null=True, blank=True)
    treating_hospital_name = models.CharField(max_length=255, null=True, blank=True)

    detailed_narration_of_ci_event = models.CharField(max_length=255, null=True, blank=True)
    details_of_past_history = models.CharField(max_length=255, null=True, blank=True)
    details_of_ci = models.CharField(max_length=255, null=True, blank=True)

    doctor_details = models.TextField(null=True, blank=True)

    # Hospitalization Details
    first_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    first_hospital_city = models.CharField(max_length=255, null=True, blank=True)
    first_doa = models.CharField(max_length=200, null=True, blank=True)
    first_dod = models.CharField(max_length=200, null=True, blank=True)
    first_diagnosis = models.TextField(null=True, blank=True)
    first_icp_findings = models.TextField(null=True, blank=True)
    second_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    second_doa = models.CharField(max_length=200, null=True, blank=True)
    second_dod = models.CharField(max_length=200, null=True, blank=True)
    second_diagnosis = models.TextField(null=True, blank=True)
    second_icp_findings = models.TextField(null=True, blank=True)

    #OPD Details
    opd_details = models.TextField(null=True, blank=True)

    # Investigation Details
    investigation_done = models.TextField(null=True, blank=True)

    # Conclusion
    conclusion = models.TextField(null=True, blank=True)

    # Intimation and Closure Dates
    date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=255, null=True, blank=True)
    investigator_name = models.CharField(max_length=255, null=True, blank=True)
    central_manager_name = models.CharField(max_length=255, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Secure Mind Illness Death Final Report - {self.claim_no}"

#SMC_LIVE
class SecureMindCriticalIllnessLiveFinalReport(models.Model):

    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID    #SMC
    # Insured Information
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    policy_inception = models.CharField(max_length=200, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    # Recommendation
    iclm_recommendation = models.TextField(null=True, blank=True)

    # Insured Visit Details
    insured_details = models.CharField(max_length=200, null=True, blank=True)
    insured_age_sex = models.CharField(max_length=50, null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)
    insured_mobile = models.CharField(max_length=15, null=True, blank=True)

    # CI Event Details
    ci_event_narration = models.TextField(null=True, blank=True)
    past_history_treatment = models.TextField(null=True, blank=True)
    ci_details = models.TextField(null=True, blank=True)

    # Employment Details
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    ghi_policy = models.CharField(max_length=255, null=True, blank=True)
    industry_check = models.CharField(max_length=255, null=True, blank=True)
    medical_leave_details = models.TextField(null=True, blank=True)

    # Other Insurance Policy
    other_policy_details = models.TextField(null=True, blank=True)
    ucv = models.CharField(max_length=255, null=True, blank=True)

    # Treating Doctor Visit
    treating_doctor_details = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_designation = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_registration = models.CharField(max_length=50, null=True, blank=True)
    treating_hospital_name = models.CharField(max_length=255, null=True, blank=True)

    detailed_narration_of_ci_event = models.CharField(max_length=255, null=True, blank=True)
    details_of_past_history = models.CharField(max_length=255, null=True, blank=True)
    details_of_ci = models.CharField(max_length=255, null=True, blank=True)

    doctor_details = models.TextField(null=True, blank=True)

    # Hospitalization Details
    first_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    first_hospital_city = models.CharField(max_length=255, null=True, blank=True)
    first_doa = models.CharField(max_length=200, null=True, blank=True)
    first_dod = models.CharField(max_length=200, null=True, blank=True)
    first_diagnosis = models.TextField(null=True, blank=True)
    first_icp_findings = models.TextField(null=True, blank=True)
    second_hospital_name = models.CharField(max_length=255, null=True, blank=True)
    second_doa = models.CharField(max_length=200, null=True, blank=True)
    second_dod = models.CharField(max_length=200, null=True, blank=True)
    second_diagnosis = models.TextField(null=True, blank=True)
    second_icp_findings = models.TextField(null=True, blank=True)

    #OPD Details
    opd_details = models.TextField(null=True, blank=True)

    # Investigation Details
    investigation_done = models.TextField(null=True, blank=True)

    # Conclusion
    conclusion = models.TextField(null=True, blank=True)

    # Intimation and Closure Dates
    date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=255, null=True, blank=True)
    investigator_name = models.CharField(max_length=255, null=True, blank=True)
    central_manager_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Secure Mind Illness Live Final Report - {self.claim_no}"

#Group Cashless
class GroupCashlessClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=255, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=255, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Group Cashless Closure Report - {self.claim_no}"

#Group Reimbursement 
class GroupReimbursementFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=255, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=255, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Group Cashless Closure Report - {self.claim_no}"

#PTD
class PermanentTotalDisabilityFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # PPD
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    claimant_name = models.CharField(max_length=100, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)
    channel_sourcing = models.CharField(max_length=200, null=True, blank=True)

    #Claimant visit
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=50, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    claimant_vist = models.CharField(max_length=200, null=True, blank=True)
    company_vist = models.CharField(max_length=300, null=True, blank=True)
    ohter_insurace = models.CharField(max_length=200 , null=True, blank=True)


    # Company Visit Details
    appointment_letter = models.CharField(max_length=100, null=True, blank=True)
    id_card = models.CharField(max_length=100, null=True, blank=True)
    salary_slip = models.CharField(max_length=100, null=True, blank=True)
    wages_register = models.CharField(max_length=100, null=True, blank=True)
    esic_pf_details = models.CharField(max_length=100, null=True, blank=True)
    attendance_register = models.CharField(max_length=100, null=True, blank=True)
    internal_safety_officer_report = models.CharField(max_length=500, null=True, blank=True)
    supervisor_details = models.CharField(max_length=500, null=True, blank=True)
    insured_work_profile = models.CharField(max_length=500, null=True, blank=True)
    wc_award_copy = models.CharField(max_length=100, null=True, blank=True)

    # Industrial Safety Officer Report
    industrial_safety_officer_report = models.CharField(max_length=500, null=True, blank=True)

    # Hospital Visit
    mlc_details = models.CharField(max_length=500, null=True, blank=True)
    pm_report_status = models.CharField(max_length=500, null=True, blank=True)
    admission_details = models.CharField(max_length=500, null=True, blank=True)
    casualty_note = models.CharField(max_length=500, null=True, blank=True)

    # Police Station Visit
    fir_details = models.CharField(max_length=500, null=True, blank=True)

    # PM Centre Visit
    pm_centre_name = models.CharField(max_length=200, null=True, blank=True)
    viscera_status = models.CharField(max_length=500, null=True, blank=True)
    pm_report_summary = models.CharField(max_length=500, null=True, blank=True)

    # Spot Visit
    photos_available = models.CharField(max_length=100, null=True, blank=True)
    witness_statements = models.CharField(max_length=500, null=True, blank=True)

    # Vicinity Check
    total_persons_inquired = models.CharField(max_length=100, null=True, blank=True)
    event_details = models.CharField(max_length=500, null=True, blank=True)

    # Media / Newspaper
    newspaper_details = models.CharField(max_length=500, null=True, blank=True)

    # Conclusion
    
    conclusion = models.TextField(null=True, blank=True)
    discrepancy_findings = models.CharField(max_length=500, null=True, blank=True)
   

    # Metadata
    intimation_date = models.CharField(max_length=100, null=True, blank=True)
    report_closed_date = models.CharField(max_length=100, null=True, blank=True)
    tat = models.CharField(max_length=100, null=True, blank=True)
    final_recommendation = models.CharField(max_length=500, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim Investigation Report - {self.claim_number}"

#Retail Cashless 
class RetailCashlessFinalReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=255, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=255, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Retail Cashless Final Report - {self.claim_no}"

#Retail Reimbursement 
class RetailReimbursementFinalReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=255, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=255, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Retail Cashless Final Report - {self.claim_no}"

#SMC HDC
class SecureMindClaimHospitalDailyCashFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    nol = models.CharField(max_length=50, null=True, blank=True)  # Nature of Los, null=True, blank=Trues
    policy_details = models.TextField(null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    hospital_name = models.CharField(max_length=100, null=True, blank=True)
    doj = models.CharField(max_length=200, null=True, blank=True)  # Date of Journe, null=True, blank=Truey
    doa = models.CharField(max_length=200, null=True, blank=True)  # Date of Admissio, null=True, blank=Truen
    dod = models.CharField(max_length=200, null=True, blank=True)  # Date of Discharg, null=True, blank=Truee
    diagnosis = models.TextField(null=True, blank=True)
    trigger = models.TextField(null=True, blank=True)
    date_of_allocation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)
    closure_tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time in days
    case_introduction = models.TextField(null=True, blank=True)
    insured_part_details = models.TextField(null=True, blank=True)
    hospital_part_details = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)
    discrepancy_findings = models.TextField(null=True, blank=True)
    recommendation = models.TextField(null=True, blank=True)
    
    final_conclusion = models.TextField(null=True, blank=True)

    intimation_date = models.TextField(null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time (TAT)
    final_recommendation = models.CharField(max_length=200, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Secure Mind Claim HDC Closure Report - {self.claim_no or 'Unknown'}"

#Specific Vector Born Diseace
class SpecificVectorBornDiseaceReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=200, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=200, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    ped_non_disclosure = models.CharField(max_length=200, null=True, blank=True)
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)

    intimation_date = models.TextField(null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time (TAT)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)
    
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Specific VEctor Born Diseace Report - {self.claim_no}"


#TRavel Final CLosure REport
class TravelFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # LOJ
    # Insured Information
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    policy_inception = models.CharField(max_length=200, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    # Recommendation
    iclm_recommendation = models.CharField(max_length=50, null=True, blank=True)

    # Insured Visit Details
    insured_details = models.TextField(null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)
    insured_mobile = models.CharField(max_length=15, null=True, blank=True)
    insured_statement = models.TextField(null=True, blank=True)

    # Employment Details
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=255, null=True, blank=True)
    travel_duration = models.CharField(max_length=255, null=True, blank=True)


    
    insured_statement = models.TextField(null=True, blank=True)
    hospital_detail_and_icp = models.TextField(null=True, blank=True)
    treating_doctor_detail = models.TextField(null=True, blank=True)
    lmo_details_and_statement = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)

    # Intimation and Closure Dates
    date_of_intimation = models.CharField(max_length=200, null=True, blank=True)
    date_of_closure = models.CharField(max_length=200, null=True, blank=True)

    # TAT and Manager Details
    central_tat_days = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=255, null=True, blank=True)
    central_manager_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ICLM Closure Report - {self.claim_no}"



#WC
class WorkmanCompensationFinalClosureReport(models.Model):

    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID # PPD
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    claimant_name = models.CharField(max_length=100, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)
    channel_sourcing = models.CharField(max_length=200, null=True, blank=True)

    #Claimant visit
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=50, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    claimant_vist = models.CharField(max_length=200, null=True, blank=True)
    company_vist = models.CharField(max_length=300, null=True, blank=True)
    ohter_insurace = models.CharField(max_length=200 , null=True, blank=True)


    # Company Visit Details
    appointment_letter = models.CharField(max_length=100, null=True, blank=True)
    id_card = models.CharField(max_length=100, null=True, blank=True)
    salary_slip = models.CharField(max_length=100, null=True, blank=True)
    wages_register = models.CharField(max_length=100, null=True, blank=True)
    esic_pf_details = models.CharField(max_length=100, null=True, blank=True)
    attendance_register = models.CharField(max_length=100, null=True, blank=True)
    internal_safety_officer_report = models.CharField(max_length=500, null=True, blank=True)
    supervisor_details = models.CharField(max_length=500, null=True, blank=True)
    insured_work_profile = models.CharField(max_length=500, null=True, blank=True)
    wc_award_copy = models.CharField(max_length=100, null=True, blank=True)

    # Industrial Safety Officer Report
    industrial_safety_officer_report = models.CharField(max_length=500, null=True, blank=True)

    # Hospital Visit
    mlc_details = models.CharField(max_length=500, null=True, blank=True)
    pm_report_status = models.CharField(max_length=500, null=True, blank=True)
    admission_details = models.CharField(max_length=500, null=True, blank=True)
    casualty_note = models.CharField(max_length=500, null=True, blank=True)

    # Police Station Visit
    fir_details = models.CharField(max_length=500, null=True, blank=True)

    # PM Centre Visit
    pm_centre_name = models.CharField(max_length=200, null=True, blank=True)
    viscera_status = models.CharField(max_length=500, null=True, blank=True)
    pm_report_summary = models.CharField(max_length=500, null=True, blank=True)

    # Spot Visit
    photos_available = models.CharField(max_length=100, null=True, blank=True)
    witness_statements = models.CharField(max_length=500, null=True, blank=True)

    # Vicinity Check
    total_persons_inquired = models.CharField(max_length=100, null=True, blank=True)
    event_details = models.CharField(max_length=500, null=True, blank=True)

    # Media / Newspaper
    newspaper_details = models.CharField(max_length=500, null=True, blank=True)

    # Conclusion
    
    conclusion = models.TextField(null=True, blank=True)
    
   

    # Metadata
    intimation_date = models.CharField(max_length=100, null=True, blank=True)
    report_closed_date = models.CharField(max_length=100, null=True, blank=True)
    tat = models.CharField(max_length=100, null=True, blank=True)
    final_recommendation = models.CharField(max_length=500, null=True, blank=True)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" Workman Compensation Final Closure Report - {self.claim_no}"

#Broken Bones
class BrokenBones(models.Model):

    
    case_id = models.CharField(max_length=255, null=True, blank=True)  # Link to Case ID
    claim_no = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    insured_name = models.CharField(max_length=100, null=True, blank=True)
    claimant_name = models.CharField(max_length=100, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    nature_of_loss = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)
    channel_sourcing = models.CharField(max_length=200, null=True, blank=True)

    # Claimant visit
    family_member = models.CharField(max_length=200, null=True, blank=True)
    relation_with_insured = models.CharField(max_length=50, null=True, blank=True)
    insured_occupation = models.CharField(max_length=200, null=True, blank=True)
    claimant_occupation = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    statement_details = models.TextField(null=True, blank=True)
    current_condition = models.CharField(max_length=200, null=True, blank=True)
    other_insurance = models.CharField(max_length=200, null=True, blank=True)

    # hospital visit
    mlc = models.CharField(max_length=200, null=True, blank=True)
    date_of_admission = models.CharField(max_length=200, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=200, null=True, blank=True)
    post_mortem = models.CharField(max_length=200, null=True, blank=True)
    hospital_visit_details = models.TextField(null=True, blank=True)
    
    # PM Center Visit
    police_verification_details = models.TextField(null=True, blank=True)
    police_final_report = models.TextField(null=True, blank=True)
    case_summary = models.TextField(null=True, blank=True)
    police_document_verified = models.TextField(null=True, blank=True)

    pm_centre_name = models.CharField(max_length=200, null=True, blank=True)
    cause_of_death = models.CharField(max_length=200, null=True, blank=True)
    viscera_status = models.CharField(max_length=200, null=True, blank=True)
    pm_verified = models.CharField(max_length=200, null=True, blank=True)

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
    registration_validity = models.CharField(max_length=200, null=True, blank=True)
    vehicle_details = models.CharField(max_length=200, null=True, blank=True)
    online_portal_check = models.CharField(max_length=200, null=True, blank=True)

    # vicinity check
    total_person_inquired = models.CharField(max_length=255, null=True, blank=True)
    event_details = models.CharField(max_length=200, null=True, blank=True)

    # media/newspaper
    media_date = models.CharField(max_length=100, null=True, blank=True)
    media_details = models.CharField(max_length=100, null=True, blank=True)

    # industry feedback
    other_insurance_company = models.CharField(max_length=200, null=True, blank=True)
    claim_status = models.CharField(max_length=200, null=True, blank=True)

    conclusion = models.TextField(null=True, blank=True)
    intimation_date = models.CharField(max_length=200, null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)
    iclm_recommendation = models.CharField(max_length=200, null=True, blank=True)

    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    state_manager_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" Broken Bones Final Closure Report - {self.claim_no}"
    
#HDC
class HospitalDailyCashFinalClosureReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
     # Claim Details
    claim_no = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    policy_type = models.CharField(max_length=50, null=True, blank=True)
    pid_trigger = models.TextField(null=True, blank=True)
    
    # Insured Details
    insured_name = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    claim_amount = models.CharField(max_length=255, null=True, blank=True)
    
    # Hospital Details
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hospital_registration = models.CharField(max_length=200, null=True, blank=True)
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=200, null=True, blank=True)
    treating_doctor_degree = models.CharField(max_length=200, null=True, blank=True)
    doctor_certificate = models.TextField(null=True, blank=True)
    
    # Patient Details
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_occupation = models.CharField(max_length=200, null=True, blank=True)
    patient_address = models.TextField(null=True, blank=True)
    patient_age = models.CharField(max_length=255, null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True, blank=True)
    patient_kyc_provided = models.BooleanField(default=False)
    date_of_admission = models.CharField(max_length=200, null=True, blank=True)
    date_of_discharge = models.CharField(max_length=200, null=True, blank=True)
    room_category = models.CharField(max_length=100, null=True, blank=True)
    presenting_complaint_duration = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    
    # Findings
    patient_findings = models.TextField(null=True, blank=True)
    hospital_findings = models.TextField(null=True, blank=True)
    ipd_register = models.TextField(null=True, blank=True)
    
    # Indoor Case Papers
    indoor_case_papers = models.TextField(null=True, blank=True)
    list_of_documents = models.TextField(null=True, blank=True)
    medical_findings = models.TextField(null=True, blank=True)
    lab_findings = models.TextField(null=True, blank=True)
    past_history_duration = models.TextField(null=True, blank=True)
    ped_non_disclosure = models.CharField(max_length=200, null=True, blank=True)
    # Discrepancy
    discrepancy_details = models.TextField(null=True, blank=True)
    
    # Conclusion
    conclusion = models.TextField(null=True, blank=True)
    
    # Final Recommendation
    final_recommendation = models.TextField(null=True, blank=True)

    intimation_date = models.TextField(null=True, blank=True)
    report_closed_date = models.CharField(max_length=200, null=True, blank=True)
    tat = models.CharField(max_length=255, null=True, blank=True)  # Turnaround Time (TAT)
    investigator_name = models.CharField(max_length=200, null=True, blank=True)
    central_manager_name = models.CharField(max_length=200, null=True, blank=True)
    
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hospital Daily Cash Final Closure Report - {self.claim_no}"

#LIC
class LicClaimInvestigationReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
    # Part A
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    date_of_commencement_policy = models.CharField(max_length=200, null=True, blank=True)
    name_and_occupation_of_insured = models.CharField(max_length=255, null=True, blank=True)
    address_of_insured = models.TextField(null=True, blank=True)
    name_of_insured_hospitalized = models.CharField(max_length=255, null=True, blank=True)
    age_of_insured = models.CharField(max_length=100, null=True, blank=True)
    hospital_name_and_address = models.CharField(max_length=255, null=True, blank=True)
    period_of_hospitalization = models.CharField(max_length=100, null=True, blank=True)
    illness_diagnosed = models.TextField(null=True, blank=True)
    date_of_surgery = models.CharField(max_length=200, null=True, blank=True)
    surgery_as_per_claim = models.CharField(max_length=255, null=True, blank=True)

    #part B
    si_no = models.CharField(max_length=200, null=True, blank=True)
    name_of_doctor_or_hospital = models.CharField(max_length=200, null=True, blank=True)
    place_of_visit = models.CharField(max_length=200, null=True, blank=True)
    date_of_visit = models.CharField(max_length=200, null=True, blank=True)

    # Field 2a: Are you satisfied with the identity of the Insured hospitalized and age?
    satisfied_with_identity_and_age = models.CharField(max_length=100, null=True, blank=True)
    
    # Field 2b: Mention any critical information related to health & habits of the Insured gathered during the enquiries.
    critical_information_health_habits = models.TextField(null=True, blank=True)

    # Field 3: Pre Existing Disease/Surgery Verification
    verified_pre_existing_disease_surgery = models.CharField(max_length=100, null=True, blank=True)
   
    # Field 4: Treatment or Tests Before Policy Start
    treatment_details_before_policy = models.TextField(null=True, blank=True)

    # Field 5: Employment & Leave Details Before Policy Start
    employed_and_leave_details = models.CharField(max_length=100, null=True, blank=True)
   
    # Field 6a: Health Insurance Scheme Details
    health_insurance_scheme_details = models.TextField(null=True, blank=True)

    # Field 6b: Health Insurance with Another Insurer
    other_health_insurer_details = models.TextField(null=True, blank=True)

    # Field 6c: Claims Made from Other Insurer
    claims_from_other_insurer_details = models.TextField(null=True, blank=True)

    # Field 7: Confirmation of Ailment and Surgery
    ailment_and_surgery_confirmation = models.CharField(max_length=200, null=True, blank=True)

    # Field 8: Surgery Confirmation in Claim Forms & Hospital Records
    surgery_performed_confirmation = models.CharField(max_length=200, null=True, blank=True)

    # Field 9: Misrepresentation in Hospital Records
    misrepresentation_in_hospital_records = models.TextField(null=True, blank=True)

    # Field 10: Any Other Information & Conclusion of Investigation
    additional_information = models.TextField(null=True, blank=True)


    # Investigating Official's Details
    investigating_official_name = models.CharField(max_length=255, null=True, blank=True)
    investigating_address = models.CharField(max_length=100, null=True, blank=True)
    investigating_designation = models.CharField(max_length=100, null=True, blank=True)
    investigation_date = models.CharField(max_length=100, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Lic claim investigation report form - {self.policy_number}"

#NAtional Insurance Investigation Report
class NationlInvestigationReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)
    # 1. Policy Details
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    policy_period = models.CharField(max_length=100, null=True, blank=True)
    sum_insured = models.CharField(max_length=255, null=True, blank=True)
    name_of_insured = models.CharField(max_length=255, null=True, blank=True)
    address_of_insured = models.TextField(null=True, blank=True)
    email_address_of_insured = models.EmailField()
    contact_number_of_insured = models.CharField(max_length=15, null=True, blank=True)
    type_of_policy = models.CharField(max_length=100, null=True, blank=True)  # NMP/NMPP/Group/Individual/Floate, null=True, blank=Truer
    agent_or_broker = models.CharField(max_length=255, null=True, blank=True)
    first_date_of_commencement = models.CharField(max_length=200, null=True, blank=True)
    original_sum_insured = models.CharField(max_length=255, null=True, blank=True)
    sum_insured_enhancement_details = models.TextField(null=True, blank=True)
    number_of_years_with_company = models.CharField(max_length=255, null=True, blank=True)

     # 2. Patient Details
    # Patient Name
    patient_name_as_per_policy = models.CharField(max_length=255, null=True, blank=True)
    patient_name_as_per_investigation = models.CharField(max_length=255, null=True, blank=True)
    verified_patient_name = models.CharField(max_length=255, null=True, blank=True)
    remarks_patient_name = models.TextField(null=True, blank=True)

    # Date of Birth / Age
    patient_dob_or_age_as_per_policy = models.CharField(max_length=100, null=True, blank=True)
    patient_dob_or_age_as_per_investigation = models.CharField(max_length=100, null=True, blank=True)
    verified_patient_dob_or_age = models.CharField(max_length=255, null=True, blank=True)
    remarks_patient_dob_or_age = models.TextField(null=True, blank=True)

    # Relation with Insured
    relation_with_insured_as_per_policy = models.CharField(max_length=100, null=True, blank=True)
    relation_with_insured_as_per_investigation = models.CharField(max_length=100, null=True, blank=True)
    verified_relation_with_insured = models.CharField(max_length=255, null=True, blank=True)
    remarks_relation_with_insured = models.TextField(null=True, blank=True)

    # Occupation of Patient
    occupation_of_patient_as_per_policy = models.CharField(max_length=255, null=True, blank=True)
    occupation_of_patient_as_per_investigation = models.CharField(max_length=255, null=True, blank=True)
    verified_occupation_of_patient = models.CharField(max_length=255, null=True, blank=True)
    remarks_occupation_of_patient = models.TextField(null=True, blank=True)

    # 3. Hospital Details
    hospital_name = models.CharField(max_length=255, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_email = models.CharField(max_length=255, null=True, blank=True)
    hospital_registration_number = models.CharField(max_length=100, null=True, blank=True)
    is_ppn_hospital = models.BooleanField(default=False)  # Whether PPN or Non-PPN
    contact_person_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person_number = models.CharField(max_length=15, null=True, blank=True)

    # 4. Claim & Ailment Details
    claim_number = models.CharField(max_length=50, null=True, blank=True)
    cashless_or_non_cashless = models.CharField(max_length=50, null=True, blank=True)  # Specify whether cashless or non-cashles, null=True, blank=Trues
    admission_datetime = models.CharField(max_length=50, null=True, blank=True)
    discharge_datetime = models.CharField(max_length=50, null=True, blank=True)
    icu_days = models.CharField(max_length=50, null=True, blank=True)
    disease_for_admission = models.TextField(null=True, blank=True)
    estimated_treatment_cost = models.CharField(max_length=50, null=True, blank=True)
    amount_authorized = models.CharField(max_length=50, null=True, blank=True)
    treating_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    treating_doctor_registration_number = models.CharField(max_length=100, null=True, blank=True)
    referral_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    referral_registration_number = models.CharField(max_length=100, null=True, blank=True)
    initial_treatment_details = models.TextField(null=True, blank=True)
    first_onset_of_symptoms_date = models.CharField(max_length=50, null=True, blank=True)
    pre_hospitalization_treatments = models.TextField(null=True, blank=True)
    post_hospitalization_treatments = models.TextField(null=True, blank=True)
    investigations_for_diagnosis = models.TextField()  # Attach documents if availablnull=True, blank=Truee

    # 5. Checklist for Investigation
    id_proof_of_insured_patient = models.CharField(max_length=255, null=True, blank=True)
    hospital_existence_and_registration = models.CharField(max_length=255, null=True, blank=True)
    admission_of_insured_patient = models.CharField(max_length=255, null=True, blank=True)
    treatment_particulars = models.CharField(max_length=255, null=True, blank=True)
    indoor_case_papers = models.CharField(max_length=255, null=True, blank=True)
    name_and_address_of_lab = models.CharField(max_length=255, null=True, blank=True)
    lab_vicinity_check = models.CharField(max_length=255, null=True, blank=True)
    lab_register_verified = models.CharField(max_length=255, null=True, blank=True)
    verification_of_bills_and_receipts = models.CharField(max_length=255, null=True, blank=True)
    medicine_shop_purchases_check = models.CharField(max_length=255, null=True, blank=True)
    signature_matching_check = models.CharField(max_length=255, null=True, blank=True)
    collection_of_ot_and_receipt_copies = models.CharField(max_length=255, null=True, blank=True)
    any_other_specify = models.CharField(max_length=255, null=True, blank=True)


    # 6. Interview Details
    interview_with_patient = models.TextField(null=True, blank=True)
    interview_with_doctor = models.TextField(null=True, blank=True)
    interview_with_neighbours_or_relatives = models.TextField(null=True, blank=True)

    # 7. List of Documents Collected (Tick Mark)
    photograph_of_patient_pan_voter_id = models.CharField(max_length=255, null=True, blank=True)
    copies_of_diagnostic_pathological_reports = models.CharField(max_length=255, null=True, blank=True)
    copies_of_indoor_documents = models.CharField(max_length=255, null=True, blank=True)
    copies_of_investigation_reports = models.CharField(max_length=255, null=True, blank=True)
    discharge_summary = models.CharField(max_length=255, null=True, blank=True)
    list_any_other = models.CharField(max_length=255, null=True, blank=True)
    # 8. Opinion of the Investigator about the Claim
    investigator_opinion = models.TextField(null=True, blank=True)

    # 9. Investigator Details
    investigator_name_designation = models.CharField(max_length=255, null=True, blank=True)
    investigator_email = models.CharField(max_length=255, null=True, blank=True)
    investigator_contact_number = models.CharField(max_length=15, null=True, blank=True)
    investigator_signature = models.CharField(max_length=255, null=True, blank=True)
    investigation_place = models.CharField(max_length=255, null=True, blank=True)
    investigation_date = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Investigation Report for Claim Number {self.claim_number}" 

#New India Investigation
class NewIndiaInvestigationReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)

    # Header / Reference Information
    ref = models.CharField(max_length=100, null=True, blank=True)  # e.g., "Ref-, null=True, blank=True"
    report_date = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Date-, null=True, blank=True"
    policy_number = models.CharField(max_length=50, null=True, blank=True)  # from header if neede, null=True, blank=Trued

    # Brief of the Case (Table with rows: Name of the Insured, Patient, Date of Birth/Age, Age Proof, Occupation)
    # Row: Name of the Insured PAtient
    brief_insured_name_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_insured_name_comments = models.CharField(max_length=255, null=True, blank=True)

   
    # Row: Date of Birth/Age
    brief_dob_age_insurer = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_investigation = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_dob_age_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Age Proof
    brief_age_proof_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_age_proof_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Occupation
    brief_occupation_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_occupation_comments = models.CharField(max_length=255, null=True, blank=True)

    # Policy Details
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    policy_holder_name_relation = models.CharField(max_length=255, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)

    # Claim Details
    doa_admission = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Admissio, null=True, blank=Truen
    dod_discharge = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Discharg, null=True, blank=Truee
    icu_admission_details = models.CharField(max_length=255, null=True, blank=True)
    cashless_non_cashless = models.CharField(max_length=50, null=True, blank=True)
    pre_auth_details = models.TextField()  # May include amount, document copies, estimate, etcnull=True, blank=True.
    diagnosis = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    hospital_name_address = models.CharField(max_length=255, null=True, blank=True)
    registration_hospital_info = models.TextField()  # Hospital registration & other detailnull=True, blank=Trues

    # Ailment Details
    onset_of_symptoms = models.CharField(max_length=50, null=True, blank=True)
    first_consultation = models.CharField(max_length=50, null=True, blank=True)
    referral_doctor_details = models.CharField(max_length=255, null=True, blank=True)
    initial_treatment_details = models.TextField(null=True, blank=True)
    pre_hosp_inv_treatment = models.TextField()  # Pre-hospital investigation and treatment detailnull=True, blank=Trues
    post_hosp_inv_treatment = models.TextField()  # Post-hospital investigation and treatment detailnull=True, blank=Trues
    investigations = models.TextField()  # Investigations (attach copies if needednull=True, blank=True)
    outcome = models.CharField(max_length=255, null=True, blank=True)

    # Checklist for Investigation (25 items; store answer as text, e.g., "Yes" or "No")
    inpatient_verification_report = models.CharField(max_length=50, null=True, blank=True)      # Inpatient Verification Repor, null=True, blank=Truet
    id_proof = models.CharField(max_length=50, null=True, blank=True)                            # ID Proo, null=True, blank=Truef
    copies_of_ipd_records = models.CharField(max_length=50, null=True, blank=True)               # Copies of IPD record, null=True, blank=Trues
    hospital_registration_status = models.CharField(max_length=50, null=True, blank=True)        # Whether the hospital is registered or no, null=True, blank=Truet
    mlc_register_check = models.CharField(max_length=50, null=True, blank=True)                  # MLC register check (for medico-legal cases, null=True, blank=True)
    mlc_registration_copy = models.CharField(max_length=50, null=True, blank=True)               # Copy of the MLC registratio, null=True, blank=Truen
    bills_and_receipts_check = models.CharField(max_length=50, null=True, blank=True)            # Check Bills and Receipt, null=True, blank=Trues
    lab_vicinity_status = models.CharField(max_length=50, null=True, blank=True)                 # Place of Lab (whether in vicinity of hospital or not, null=True, blank=True)
    lab_register_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of Lab Registe, null=True, blank=Truer
    lab_register_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Lab Registe, null=True, blank=Truer
    medicine_shop_location = models.CharField(max_length=50, null=True, blank=True)              # Place of medicine's shop (whether in vicinity of hospital or not, null=True, blank=True)
    receipt_book_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of receipt book of medicine, null=True, blank=Trues
    receipt_book_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Receipt Boo, null=True, blank=Truek
    tests_at_hospital_check = models.CharField(max_length=50, null=True, blank=True)             # Check Tests done at Hospita, null=True, blank=Truel
    tests_at_diagnostic_centre_check = models.CharField(max_length=50, null=True, blank=True)      # Check Tests done at Diagnostic Centr, null=True, blank=Truee
    medicines_dispensed_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines dispensed from hospita, null=True, blank=Truel
    medicines_purchased_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines purchased from sho, null=True, blank=Truep
    signature_verification = models.CharField(max_length=50, null=True, blank=True)              # Check Signature patient verifie, null=True, blank=Trued
    ot_register_copy = models.CharField(max_length=50, null=True, blank=True)                    # Copy of OT Register Take, null=True, blank=Truen
    hospital_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)      # Hospital's lab register verifie, null=True, blank=Trued
    centre_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)        # Centre’s lab register verifie, null=True, blank=Trued
    bills_at_hospital_verified = models.CharField(max_length=50, null=True, blank=True)          # Copy of Bills at Hospital Verifie, null=True, blank=Trued
    bills_at_shop_verified = models.CharField(max_length=50, null=True, blank=True)              # Copy of Bills at shop verified (close to Hospital, null=True, blank=True)
    treating_doctor_credentials = models.CharField(max_length=50, null=True, blank=True)         # Verification of treating doctor’s credential, null=True, blank=Trues
    signature_matching = models.CharField(max_length=50, null=True, blank=True)                  # Whether Signature Matching – Doctor, claimant & Life Insure, null=True, blank=Trued

    # Insured's Address Details
    insured_address_details = models.TextField(null=True, blank=True)

    # Insured's Interview
    insured_interview = models.TextField(null=True, blank=True)
    opinion = models.TextField(null=True, blank=True)
 

    # List of Collected Documents
    collected_documents = models.TextField()  # e.g., photograph, PAN/Voter ID, copies of tests, case papers, etcnull=True, blank=True.

    # Report Generated By
    report_generated_by_name = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_designation = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_mobile = models.CharField(max_length=50, null=True, blank=True)
    report_generated_by_email = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_web_address = models.CharField(max_length=255, null=True, blank=True)
    report_generated_date = models.CharField(max_length=50, null=True, blank=True)
    report_generated_place = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Investigation Report - Policy No: {self.policy_number}"

#Oriental Format Investigation
class OrientalFormatInvestigationReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)

    # Header / Reference Information
    ref = models.CharField(max_length=100, null=True, blank=True)  # e.g., "Ref-, null=True, blank=True"
    report_date = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Date-, null=True, blank=True"
    policy_number = models.CharField(max_length=50, null=True, blank=True)  # from header if neede, null=True, blank=Trued

    # Brief of the Case (Table with rows: Name of the Insured, Patient, Date of Birth/Age, Age Proof, Occupation)
    # Row: Name of the Insured PAtient
    brief_insured_name_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_insured_name_comments = models.CharField(max_length=255, null=True, blank=True)

   
    # Row: Date of Birth/Age
    brief_dob_age_insurer = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_investigation = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_dob_age_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Age Proof
    brief_age_proof_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_age_proof_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Occupation
    brief_occupation_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_occupation_comments = models.CharField(max_length=255, null=True, blank=True)

    # Policy Details
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    policy_holder_name_relation = models.CharField(max_length=255, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)

    # Claim Details
    doa_admission = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Admissio, null=True, blank=Truen
    dod_discharge = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Discharg, null=True, blank=Truee
    icu_admission_details = models.CharField(max_length=255, null=True, blank=True)
    cashless_non_cashless = models.CharField(max_length=50, null=True, blank=True)
    pre_auth_details = models.TextField()  # May include amount, document copies, estimate, etcnull=True, blank=True.
    diagnosis = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    hospital_name_address = models.CharField(max_length=255, null=True, blank=True)
    registration_hospital_info = models.TextField()  # Hospital registration & other detailnull=True, blank=Trues

    # Ailment Details
    onset_of_symptoms = models.CharField(max_length=50, null=True, blank=True)
    first_consultation = models.CharField(max_length=50, null=True, blank=True)
    referral_doctor_details = models.CharField(max_length=255, null=True, blank=True)
    initial_treatment_details = models.TextField(null=True, blank=True)
    pre_hosp_inv_treatment = models.TextField()  # Pre-hospital investigation and treatment detailnull=True, blank=Trues
    post_hosp_inv_treatment = models.TextField()  # Post-hospital investigation and treatment detailnull=True, blank=Trues
    investigations = models.TextField()  # Investigations (attach copies if needednull=True, blank=True)
    outcome = models.CharField(max_length=255, null=True, blank=True)

    # Checklist for Investigation (25 items; store answer as text, e.g., "Yes" or "No")
    inpatient_verification_report = models.CharField(max_length=50, null=True, blank=True)      # Inpatient Verification Repor, null=True, blank=Truet
    id_proof = models.CharField(max_length=50, null=True, blank=True)                            # ID Proo, null=True, blank=Truef
    copies_of_ipd_records = models.CharField(max_length=50, null=True, blank=True)               # Copies of IPD record, null=True, blank=Trues
    hospital_registration_status = models.CharField(max_length=50, null=True, blank=True)        # Whether the hospital is registered or no, null=True, blank=Truet
    mlc_register_check = models.CharField(max_length=50, null=True, blank=True)                  # MLC register check (for medico-legal cases, null=True, blank=True)
    mlc_registration_copy = models.CharField(max_length=50, null=True, blank=True)               # Copy of the MLC registratio, null=True, blank=Truen
    bills_and_receipts_check = models.CharField(max_length=50, null=True, blank=True)            # Check Bills and Receipt, null=True, blank=Trues
    lab_vicinity_status = models.CharField(max_length=50, null=True, blank=True)                 # Place of Lab (whether in vicinity of hospital or not, null=True, blank=True)
    lab_register_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of Lab Registe, null=True, blank=Truer
    lab_register_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Lab Registe, null=True, blank=Truer
    medicine_shop_location = models.CharField(max_length=50, null=True, blank=True)              # Place of medicine's shop (whether in vicinity of hospital or not, null=True, blank=True)
    receipt_book_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of receipt book of medicine, null=True, blank=Trues
    receipt_book_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Receipt Boo, null=True, blank=Truek
    tests_at_hospital_check = models.CharField(max_length=50, null=True, blank=True)             # Check Tests done at Hospita, null=True, blank=Truel
    tests_at_diagnostic_centre_check = models.CharField(max_length=50, null=True, blank=True)      # Check Tests done at Diagnostic Centr, null=True, blank=Truee
    medicines_dispensed_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines dispensed from hospita, null=True, blank=Truel
    medicines_purchased_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines purchased from sho, null=True, blank=Truep
    signature_verification = models.CharField(max_length=50, null=True, blank=True)              # Check Signature patient verifie, null=True, blank=Trued
    ot_register_copy = models.CharField(max_length=50, null=True, blank=True)                    # Copy of OT Register Take, null=True, blank=Truen
    hospital_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)      # Hospital's lab register verifie, null=True, blank=Trued
    centre_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)        # Centre’s lab register verifie, null=True, blank=Trued
    bills_at_hospital_verified = models.CharField(max_length=50, null=True, blank=True)          # Copy of Bills at Hospital Verifie, null=True, blank=Trued
    bills_at_shop_verified = models.CharField(max_length=50, null=True, blank=True)              # Copy of Bills at shop verified (close to Hospital, null=True, blank=True)
    treating_doctor_credentials = models.CharField(max_length=50, null=True, blank=True)         # Verification of treating doctor’s credential, null=True, blank=Trues
    signature_matching = models.CharField(max_length=50, null=True, blank=True)                  # Whether Signature Matching – Doctor, claimant & Life Insure, null=True, blank=Trued

    # Insured's Address Details
    insured_address_details = models.TextField(null=True, blank=True)

    # Insured's Interview
    insured_interview = models.TextField(null=True, blank=True)
    opinion = models.TextField(null=True, blank=True)
 

    # List of Collected Documents
    collected_documents = models.TextField()  # e.g., photograph, PAN/Voter ID, copies of tests, case papers, etcnull=True, blank=True.

    # Report Generated By
    report_generated_by_name = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_designation = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_mobile = models.CharField(max_length=50, null=True, blank=True)
    report_generated_by_email = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_web_address = models.CharField(max_length=255, null=True, blank=True)
    report_generated_date = models.CharField(max_length=50, null=True, blank=True)
    report_generated_place = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Oriental Format Investigation Report - Policy No: {self.policy_number}"
    
#United India Investigation
class UnitedIndiaInvestigationReport(models.Model):

    case_id = models.CharField(max_length=255, null=True, blank=True)

    # Header / Reference Information
    ref = models.CharField(max_length=100, null=True, blank=True)  # e.g., "Ref-, null=True, blank=True"
    report_date = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Date-, null=True, blank=True"
    policy_number = models.CharField(max_length=50, null=True, blank=True)  # from header if neede, null=True, blank=Trued

    # Brief of the Case (Table with rows: Name of the Insured, Patient, Date of Birth/Age, Age Proof, Occupation)
    # Row: Name of the Insured PAtient
    brief_insured_name_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_insured_name_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_insured_name_comments = models.CharField(max_length=255, null=True, blank=True)

   
    # Row: Date of Birth/Age
    brief_dob_age_insurer = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_investigation = models.CharField(max_length=100, null=True, blank=True)
    brief_dob_age_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_dob_age_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Age Proof
    brief_age_proof_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_age_proof_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_age_proof_comments = models.CharField(max_length=255, null=True, blank=True)

    # Row: Occupation
    brief_occupation_insurer = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_investigation = models.CharField(max_length=255, null=True, blank=True)
    brief_occupation_verified = models.CharField(max_length=50, null=True, blank=True)
    brief_occupation_comments = models.CharField(max_length=255, null=True, blank=True)

    # Policy Details
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    policy_holder_name_relation = models.CharField(max_length=255, null=True, blank=True)
    policy_type = models.CharField(max_length=100, null=True, blank=True)

    # Claim Details
    doa_admission = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Admissio, null=True, blank=Truen
    dod_discharge = models.CharField(max_length=50, null=True, blank=True)  # Date and Time of Discharg, null=True, blank=Truee
    icu_admission_details = models.CharField(max_length=255, null=True, blank=True)
    cashless_non_cashless = models.CharField(max_length=50, null=True, blank=True)
    pre_auth_details = models.TextField()  # May include amount, document copies, estimate, etcnull=True, blank=True.
    diagnosis = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    hospital_name_address = models.CharField(max_length=255, null=True, blank=True)
    registration_hospital_info = models.TextField()  # Hospital registration & other detailnull=True, blank=Trues

    # Ailment Details
    onset_of_symptoms = models.CharField(max_length=50, null=True, blank=True)
    first_consultation = models.CharField(max_length=50, null=True, blank=True)
    referral_doctor_details = models.CharField(max_length=255, null=True, blank=True)
    initial_treatment_details = models.TextField(null=True, blank=True)
    pre_hosp_inv_treatment = models.TextField()  # Pre-hospital investigation and treatment detailnull=True, blank=Trues
    post_hosp_inv_treatment = models.TextField()  # Post-hospital investigation and treatment detailnull=True, blank=Trues
    investigations = models.TextField()  # Investigations (attach copies if needednull=True, blank=True)
    outcome = models.CharField(max_length=255, null=True, blank=True)

    # Checklist for Investigation (25 items; store answer as text, e.g., "Yes" or "No")
    inpatient_verification_report = models.CharField(max_length=50, null=True, blank=True)      # Inpatient Verification Repor, null=True, blank=Truet
    id_proof = models.CharField(max_length=50, null=True, blank=True)                            # ID Proo, null=True, blank=Truef
    copies_of_ipd_records = models.CharField(max_length=50, null=True, blank=True)               # Copies of IPD record, null=True, blank=Trues
    hospital_registration_status = models.CharField(max_length=50, null=True, blank=True)        # Whether the hospital is registered or no, null=True, blank=Truet
    mlc_register_check = models.CharField(max_length=50, null=True, blank=True)                  # MLC register check (for medico-legal cases, null=True, blank=True)
    mlc_registration_copy = models.CharField(max_length=50, null=True, blank=True)               # Copy of the MLC registratio, null=True, blank=Truen
    bills_and_receipts_check = models.CharField(max_length=50, null=True, blank=True)            # Check Bills and Receipt, null=True, blank=Trues
    lab_vicinity_status = models.CharField(max_length=50, null=True, blank=True)                 # Place of Lab (whether in vicinity of hospital or not, null=True, blank=True)
    lab_register_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of Lab Registe, null=True, blank=Truer
    lab_register_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Lab Registe, null=True, blank=Truer
    medicine_shop_location = models.CharField(max_length=50, null=True, blank=True)              # Place of medicine's shop (whether in vicinity of hospital or not, null=True, blank=True)
    receipt_book_check = models.CharField(max_length=50, null=True, blank=True)                  # Checking of receipt book of medicine, null=True, blank=Trues
    receipt_book_photocopy = models.CharField(max_length=50, null=True, blank=True)              # Photocopy of Receipt Boo, null=True, blank=Truek
    tests_at_hospital_check = models.CharField(max_length=50, null=True, blank=True)             # Check Tests done at Hospita, null=True, blank=Truel
    tests_at_diagnostic_centre_check = models.CharField(max_length=50, null=True, blank=True)      # Check Tests done at Diagnostic Centr, null=True, blank=Truee
    medicines_dispensed_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines dispensed from hospita, null=True, blank=Truel
    medicines_purchased_check = models.CharField(max_length=50, null=True, blank=True)           # Check Medicines purchased from sho, null=True, blank=Truep
    signature_verification = models.CharField(max_length=50, null=True, blank=True)              # Check Signature patient verifie, null=True, blank=Trued
    ot_register_copy = models.CharField(max_length=50, null=True, blank=True)                    # Copy of OT Register Take, null=True, blank=Truen
    hospital_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)      # Hospital's lab register verifie, null=True, blank=Trued
    centre_lab_register_verified = models.CharField(max_length=50, null=True, blank=True)        # Centre’s lab register verifie, null=True, blank=Trued
    bills_at_hospital_verified = models.CharField(max_length=50, null=True, blank=True)          # Copy of Bills at Hospital Verifie, null=True, blank=Trued
    bills_at_shop_verified = models.CharField(max_length=50, null=True, blank=True)              # Copy of Bills at shop verified (close to Hospital, null=True, blank=True)
    treating_doctor_credentials = models.CharField(max_length=50, null=True, blank=True)         # Verification of treating doctor’s credential, null=True, blank=Trues
    signature_matching = models.CharField(max_length=50, null=True, blank=True)                  # Whether Signature Matching – Doctor, claimant & Life Insure, null=True, blank=Trued

    # Insured's Address Details
    insured_address_details = models.TextField(null=True, blank=True)

    # Insured's Interview
    insured_interview = models.TextField(null=True, blank=True)
    opinion = models.TextField(null=True, blank=True)
 

    # List of Collected Documents
    collected_documents = models.TextField()  # e.g., photograph, PAN/Voter ID, copies of tests, case papers, etcnull=True, blank=True.

    # Report Generated By
    report_generated_by_name = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_designation = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_mobile = models.CharField(max_length=50, null=True, blank=True)
    report_generated_by_email = models.CharField(max_length=255, null=True, blank=True)
    report_generated_by_web_address = models.CharField(max_length=255, null=True, blank=True)
    report_generated_date = models.CharField(max_length=50, null=True, blank=True)
    report_generated_place = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"United India Investigation Report - Policy No: {self.policy_number}"
    
#Other Insurance Investigation
class OtherInsuranceInvestigationReport(models.Model):
    case_id = models.CharField(max_length=255, null=True, blank=True)

    # Header Information
    name_of_the_insured = models.CharField(max_length=255, null=True, blank=True)
    our_ref_no = models.CharField(max_length=100, null=True, blank=True)
    your_ref_no = models.CharField(max_length=100, null=True, blank=True)
    policy_inception_date = models.CharField(max_length=50, null=True, blank=True)
    type_of_claim = models.CharField(max_length=100, null=True, blank=True)
    hospital_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    claim_amount = models.CharField(max_length=50, null=True, blank=True)
    date_of_investigation_assigned = models.CharField(max_length=50, null=True, blank=True)
    date_of_report_sent = models.CharField(max_length=50, null=True, blank=True)
    tat = models.CharField(max_length=50, null=True, blank=True)
    triggers = models.CharField(max_length=255, null=True, blank=True)
    
    # INSURED & RELATED DETAILS
    proposer_name = models.CharField(max_length=255, null=True, blank=True)
    patient_name_insured = models.CharField(max_length=255, null=True, blank=True)
    insured_residential_address = models.TextField()  # full address, including contact numbernull=True, blank=Trues
    insured_mobile_no = models.CharField(max_length=50, null=True, blank=True)
    occupation_of_insured = models.CharField(max_length=255, null=True, blank=True)
    distance_from_hospital = models.CharField(max_length=100, null=True, blank=True)  # e.g., "10 km, null=True, blank=True"
    reason_for_selecting_hospital = models.TextField(null=True, blank=True)
    other_hospitals_in_between = models.CharField(max_length=255, null=True, blank=True)  # e.g., "Yes/No" or list name, null=True, blank=Trues
    family_physician_details = models.CharField(max_length=255, null=True, blank=True)
    policies_with_us = models.CharField(max_length=50, null=True, blank=True)
    policies_with_others = models.CharField(max_length=50, null=True, blank=True)
    earlier_claims_details = models.TextField()  # details of earlier claimnull=True, blank=Trues
    
    # HOSPITAL & DOCTOR RELATED
    inpatient_beds = models.CharField(max_length=50, null=True, blank=True)
    hospital_registration_number = models.CharField(max_length=100, null=True, blank=True)
    hospital_facilities = models.CharField(max_length=255, null=True, blank=True)  # details of OT, lab, store, etc, null=True, blank=True.
    doctor_qualification = models.CharField(max_length=255, null=True, blank=True)  # e.g., "Dr. John Doe, null=True, blank=True"
    doctor_reg_no = models.CharField(max_length=100, null=True, blank=True)
    no_of_rmos_doctors_nurses = models.CharField(max_length=50, null=True, blank=True)
    room_rent_tariff_options = models.TextField(null=True, blank=True)
    
    # FOR DISEASE RELATED CLAIMS
    main_symptoms = models.TextField(null=True, blank=True)
    doa = models.CharField(max_length=50, null=True, blank=True)  # Date of Admissio, null=True, blank=Truen
    dod = models.CharField(max_length=50, null=True, blank=True)  # Date of Discharg, null=True, blank=Truee
    line_of_treatment = models.CharField(max_length=255, null=True, blank=True)
    name_of_surgeon_and_anesthetist = models.CharField(max_length=255, null=True, blank=True)
    type_of_anesthesia = models.CharField(max_length=100, null=True, blank=True)
    justified_or_prolonged_stay = models.CharField(max_length=255, null=True, blank=True)
    medical_surgical_history = models.TextField(null=True, blank=True)
    previous_similar_history = models.CharField(max_length=255, null=True, blank=True)
    doctor_opinion_duration = models.CharField(max_length=255, null=True, blank=True)
    diagnostic_tests_aligned = models.CharField(max_length=255, null=True, blank=True)
    
    # ACCIDENT RELATED CLAIMS
    accident_date_time = models.CharField(max_length=50, null=True, blank=True)
    accident_narration = models.TextField(null=True, blank=True)
    pa_policy_status = models.CharField(max_length=50, null=True, blank=True)
    fir_mlc_status = models.CharField(max_length=50, null=True, blank=True)
    scar_mark_verification_acc = models.CharField(max_length=255, null=True, blank=True)
    alcoholism_factor = models.CharField(max_length=50, null=True, blank=True)
    accident_type = models.CharField(max_length=100, null=True, blank=True)
    prolonged_stay_reason = models.TextField(null=True, blank=True)
    doctor_opinion_accident = models.TextField(null=True, blank=True)
    
    # VERIFICATION FROM HOSPITAL
    indoor_register_verified = models.CharField(max_length=50, null=True, blank=True)
    date_overwriting_in_register = models.CharField(max_length=50, null=True, blank=True)
    ipd_papers_continuity = models.CharField(max_length=50, null=True, blank=True)
    hospital_bills_inflation = models.CharField(max_length=50, null=True, blank=True)
    
    # VERIFICATION FROM MEDICAL STORE
    medical_bills_verified = models.CharField(max_length=50, null=True, blank=True)
    medicines_match_ipd = models.CharField(max_length=50, null=True, blank=True)
    store_bills_inflation = models.CharField(max_length=50, null=True, blank=True)
    
    # VERIFICATION FROM PATHOLOGY LAB
    investigation_reports_verified = models.CharField(max_length=50, null=True, blank=True)
    lab_register_verified = models.CharField(max_length=50, null=True, blank=True)
    investigations_match_ipd = models.CharField(max_length=50, null=True, blank=True)
    lab_bills_inflation = models.CharField(max_length=50, null=True, blank=True)


    lab_observations = models.TextField(null=True, blank=True)
    
    # Discharge Summary, ICP’s and Doctor Statement
    discharge_and_doctor_statement = models.TextField(null=True, blank=True)
    
    # As per Lab Report
    lab_report_date = models.CharField(max_length=50, null=True, blank=True)
    
    # Blood Count
    hb = models.CharField(max_length=50, null=True, blank=True)
    wbc = models.CharField(max_length=50, null=True, blank=True)
    rbc = models.CharField(max_length=50, null=True, blank=True)
    plt = models.CharField(max_length=50, null=True, blank=True)
    
    # Duration of Chronic Disease
    chronic_disease_duration = models.CharField(max_length=100, null=True, blank=True)
    genuinity_of_claim = models.CharField(max_length=255, null=True, blank=True)
    final_doctor_qualification = models.CharField(max_length=255, null=True, blank=True)
    final_doctor_reg_no = models.CharField(max_length=100, null=True, blank=True)
    hospital_norms = models.CharField(max_length=255, null=True, blank=True)
    bills_inflation = models.CharField(max_length=50, null=True, blank=True)
    med_store_bill_verification = models.CharField(max_length=50, null=True, blank=True)
    final_scar_mark_verification = models.CharField(max_length=50, null=True, blank=True)
    
    # Remarks & Final Decision
    remarks = models.TextField(null=True, blank=True)
    
    # Report Generated By
    medical_officer_name =models.CharField(max_length=200, null=True, blank=True)
    
    # Enclosures (list of documents confirmed and verified)
    enclosures = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Investigation Report: {self.name_of_the_insured} - Policy No: {self.your_ref_no}"
