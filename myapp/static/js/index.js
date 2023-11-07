
const listUsersNornir = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/listusersnornir2/')
        const data = await response.json()
        console.log(response)
        console.log(data)

        let content = ``
        data.usuarios_nornir.forEach((user, index) => {
            let staffRole = '';
            if (user.is_staff == true) {
                staffRole = "administrador";
            } else {
                staffRole = "consultor";
            }
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${user.username}</td>
                    <td>${user.last_name}</td>
                    <td>${staffRole}</td>
                </tr>
            `
        })
        tableBody_usersnornir.innerHTML = content
    } catch (ex) {
        alert(ex)
    }
}

window.addEventListener("load", async () => {
    await listUsersNornir()
})
