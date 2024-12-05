function processStep(step_number) {
    for (let i = 1; i <= 6; i++) {
        document.getElementById(`step-${i}`).style.display = 'none';
    }
    if (step_number == 1) {
        document.getElementById('step-name').innerHTML = 'Case Details';
    }

    if (step_number == 2) {
        document.getElementById('step-name').innerHTML = 'Investigation';
    }

    if (step_number == 3) {
        document.getElementById('step-name').innerHTML = 'Medical Remarks';
    }

    if (step_number == 4) {
        document.getElementById('step-name').innerHTML = 'Final Report';
    }

    if (step_number == 5) {
        document.getElementById('step-name').innerHTML = 'Case Submission';
    }

    if (step_number == 6) {
        document.getElementById('step-name').innerHTML = 'Case Closed';
    }

    let step_id = `step-${step_number}`
    let step_ele = document.getElementById(step_id);
    step_ele.style.display = '';
}
