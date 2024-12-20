
function toggleCard(card) {
    let card_id = card.id;
    let card_detial_id = `${card_id}-detail`;
    let card_icon_id = `${card_id}-icon`;
    let card_details_ele = document.getElementById(card_detial_id);
    console.log(card_detial_id);
    if (card_details_ele.style.display == 'none') {
        card_details_ele.style.display = 'block';
        document.getElementById(card_icon_id).classList.remove('fa-plus');
        document.getElementById(card_icon_id).classList.add('fa-minus');
    }
    else {
        card_details_ele.style.display = 'none';
        document.getElementById(card_icon_id).classList.remove('fa-minus');
        document.getElementById(card_icon_id).classList.add('fa-plus');
    }
}

function handleOptionChange() {
    const select = document.getElementById('type_of_visit');
    const selectedValue = select.value;

    if (selectedValue === 'Hospital') {
        createHospitalFormInput();
    }

    if (selectedValue === 'Lab') {
        createLabFormInput();
    }

    if (selectedValue === 'Chemist') {
        createChemistFormInput();
    }

    if (selectedValue === 'default') {
        deleteElementsWithIdPrefix('type_visit_');
    }

}

function createInputDiv(containerId, inputId, labelText, placeholderText) {
    const div = document.createElement('div');
    div.className = 'mb-3';
    div.id = containerId;

    const label = document.createElement('label');
    label.htmlFor = inputId;
    label.className = 'form-label eh-label';
    label.textContent = labelText;

    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'form-control dark-input';
    input.id = inputId;
    input.name = inputId;
    input.placeholder = placeholderText;

    div.appendChild(label);
    div.appendChild(input);

    return div;
}

function deleteElementsWithIdPrefix(prefix) {
    const elements = document.querySelectorAll(`[id^="${prefix}"]`);
    elements.forEach(element => element.remove());
}

function createHospitalFormInput() {
    deleteElementsWithIdPrefix('type_visit_');
    const parentElement = document.getElementById('add_visit_form_inputs');
    parentElement.appendChild(createInputDiv('type_visit_hospital_hospital_name', 'hospital_hospital_name', 'Hospital Name', 'Enter Hospital Name'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_state', 'hospital_state', 'State', 'Enter State'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_city', 'hospital_city', 'City', 'Enter City'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_doa', 'hospital_doa', 'Date of Admission', 'Enter Date of Admission'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_dod', 'hospital_dod', 'Date of Discharge', 'Enter Date of Discharge'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_claim_value', 'hospital_claim_value', 'Claim Value', 'Enter Claim Value'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_diagnosis', 'hospital_diagnosis', 'Diagnosis', 'Enter Diagnosis'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_registration_number', 'hospital_registration_number', 'Registration Number', 'Enter Registration Number'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_no_of_beds', 'hospital_no_of_beds', 'No of Beds', 'Enter No of Beds'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_icu', 'hospital_icu', 'ICU', 'Enter ICU'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_ot', 'hospital_ot', 'OT', 'Enter OT'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_nursing_staff', 'hospital_nursing_staff', 'Nursing staff', 'Enter Nursing staff'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_rmo', 'hospital_rmo', 'RMO', 'Enter RMO'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_td_registration_number', 'hospital_td_registration_number', 'TD registration number', 'Enter TD registration number'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_degree', 'hospital_degree', 'Degree', 'Enter Degree'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_owner_of_the_hospital', 'hospital_owner_of_the_hospital', 'Owner of the hospital', 'Enter Owner of the hospital'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_doctor_registration_number', 'hospital_doctor_registration_number', 'Registration Number', 'Enter Registration Number'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_doctor_contact_number', 'hospital_doctor_contact_number', 'Contact Number', 'Enter Contact Number'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_doctor_email', 'hospital_doctor_email', 'Email Id', 'Enter Email Id'));
    parentElement.appendChild(createInputDiv('type_visit_hospital_tat', 'hospital_tat', 'TAT', 'Enter TAT'));

}

function createLabFormInput() {
    deleteElementsWithIdPrefix('type_visit_');
    const parentElement = document.getElementById('add_visit_form_inputs');
    parentElement.appendChild(createInputDiv('type_visit_lab_name', 'lab_name', 'Name', 'Enter Name'));
    parentElement.appendChild(createInputDiv('type_visit_lab_city', 'lab_city', 'City', 'Enter City'));
    parentElement.appendChild(createInputDiv('type_visit_lab_state', 'lab_state', 'State', 'Enter State'));
    parentElement.appendChild(createInputDiv('type_visit_lab_address', 'lab_address', 'Address', 'Enter Address'));
    parentElement.appendChild(createInputDiv('type_visit_lab_pathologist_name', 'lab_pathologist_name', 'Pathologist Name', 'Enter Pathologist Name'));
    parentElement.appendChild(createInputDiv('type_visit_lab_registration_number', 'lab_registration_number', 'Registration Number', 'Enter Registration Number'));
    parentElement.appendChild(createInputDiv('type_visit_lab_tat', 'lab_tat', 'TAT', 'Enter TAT'));

}

function createChemistFormInput() {
    deleteElementsWithIdPrefix('type_visit_');
    const parentElement = document.getElementById('add_visit_form_inputs');
    parentElement.appendChild(createInputDiv('type_visit_chemist_name_of_chemist', 'chemist_name_of_chemist', 'Name of Chemist', 'Enter Name of Chemist'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_address', 'chemist_address', 'Address', 'Enter Address'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_state', 'chemist_state', 'State', 'Enter State'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_city', 'chemist_city', 'City', 'Enter City'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_gst_number', 'chemist_gst_number', 'GST Number', 'Enter GST Number'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_drug_license_number', 'chemist_drug_license_number', 'Drug Licence Number', 'Enter Drug Licence Number'));
    parentElement.appendChild(createInputDiv('type_visit_chemist_tat', 'chemist_tat', 'TAT', 'Enter TAT'));

}

function toggleAddQuestions() {
    let question_list = document.getElementById('questions-list');

    if (question_list.style.display == 'none') {
        question_list.style.display = 'block';
        document.getElementById('add-question-icon').classList.remove('fa-chevron-down');
        document.getElementById('add-question-icon').classList.add('fa-chevron-up');
    }
    else {
        question_list.style.display = 'none';
        document.getElementById('add-question-icon').classList.remove('fa-chevron-up');
        document.getElementById('add-question-icon').classList.add('fa-chevron-down');
    }
}

function generateQuestions(questions) {
    const container = document.getElementById('questions-list'); // Create a container for the checkboxes
    questions.forEach((question, index) => {
        const questionNumber = index + 1; // Calculate the question number

        // Create the outer div with class "form-check"
        const div = document.createElement('div');
        div.className = 'form-check';

        const input = document.createElement('input');
        input.type = 'checkbox';
        input.className = 'form-check-input eh-checkbox';
        input.id = `visit_question${questionNumber}`;
        input.name = `question${questionNumber}`;
        input.value = question.id;

        const label = document.createElement('label');
        label.className = 'form-check-label';
        label.setAttribute('for', `visit_question${questionNumber}`);
        label.textContent = question.question;

        div.appendChild(input);
        div.appendChild(label);

        container.appendChild(div);

        const hr = document.createElement('hr');
        hr.className = 'my-2';
        container.appendChild(hr);
    });
}

function viewQuestions(questions) {
    let question_list = document.getElementById(`${questions.id}-list`);

    if (question_list.style.display == 'none') {
        question_list.style.display = 'block';
        document.getElementById(`${questions.id}-icon`).classList.remove('fa-chevron-down');
        document.getElementById(`${questions.id}-icon`).classList.add('fa-chevron-up');
    }
    else {
        question_list.style.display = 'none';
        document.getElementById(`${questions.id}-icon`).classList.remove('fa-chevron-up');
        document.getElementById(`${questions.id}-icon`).classList.add('fa-chevron-down');
    }
}
