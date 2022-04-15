const confirmPass = document.querySelector('#confirmpass');
const error = document.querySelector("#error")
confirmPass.addEventListener('input', (event) => {
    const pass = document.querySelector("#pass")
    if (pass.value != event.target.value) {
        error.innerText = "Password not matching."
    } else {
        error.innerText = ""
    }
});
const pass = document.querySelector('#pass');
pass.addEventListener('input', (event) => {
    const confirmPass = document.querySelector("#confirmpass")
    if (confirmPass.value != event.target.value) {
        error.innerText = "Password not matching."
    } else {
        error.innerText = ""
    }
});