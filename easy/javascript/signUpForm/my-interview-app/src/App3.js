
//19min!

import { useState } from "react";
import "./styles.css"

function API(data) {
    return new Promise((resolve) => {
        const isRepeated = data.email === "repeated@gmail.com";
        setTimeout(() => {
            resolve({
                status: isRepeated ? "ERROR" : "OK",
                message: isRepeated ? "Email is already taken" : "Signup successful!"
            });
        }, 1000);
    });
}

export default function App3(){

    const [status, setStatus] = useState();
    const [loading,setLoading] = useState(false);

    async function handleSubmission(event) {

        event.preventDefault();
        setLoading(true);

        let data = Object.fromEntries(new FormData(event.target));

        let isEmailValid = data.email 
        && data.email.includes("@")
        && data.email.split("@")[1].includes(".");

        let isPasswordValid = data.password
        && data.password.length >= 8
        && /[0-9]/.test(data.password)
        && /[^A-Za-z0-9]/.test(data.password);

        if(!isEmailValid) {
            setStatus({
                message: "Email is invalid!",
                type: "error"
            })
            setLoading(false);
            return;
        }

        if(!isPasswordValid) {
            setStatus({
                message: "Password is invalid!",
                type: "error"
            })
            setLoading(false);
            return;
        }

        try{
            let res = await API(data);
            setStatus({message: res.message, type: res.status == "OK" ? "success": "error"})

        } catch(err) {
            setStatus({message: "Server error", type: "error"})
        } finally {
            setLoading(false);
        }

    }


    return (
        <div className="App3">
            <h1>Log in</h1>
            <form onSubmit={handleSubmission} method="POST">
                <input name="email" type="email"></input>
                <input name="password" type="password"></input>
                <button disabled={loading}>{loading ? "Loading" : "Submit"}</button>

            {status && (
                <div className={status.type}>{status.message}</div>
            )}
            </form>

        </div>
    )
}