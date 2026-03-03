/*
Build a user Signup form in React with the following features.

1. An email and a password input X
2. Email must have an "@" and the domain side must include a "."
3. Password must include
    1. at least one special character
    2. one number and be at least 8 characters
4. Submission request handling
    1. Utilze the mock API function to handle submissions
5. Basic aesthetics with pure CSS
*/

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



export default function App2() {
    const [status,setStatus] = useState();
    const [loading, setLoading] = useState(false);

    async function handleSubmission(event) {
        event.preventDefault();
       setLoading(true);
       let  data = Object.fromEntries(new FormData(event.target));

       let isEmailValid = data.email
        && data.email.includes("@")
        && data.email.split("@")[1].includes(".");
       let isPasswordValid = data.password
            && data.password.length >=8 
            && /[0-9]/.test(data.password)
            && /[^A-Za-z0-9]/.test(data.password);

        if(!isEmailValid) {
            setStatus({
                message: "Email is invalid!",
                type:"error"
            })
            setLoading(false);
            return;
        }

        if(!isPasswordValid) {
            setStatus({
                message: "Password is invalid!",
                type:"error"
            });
            setLoading(false);
            return;
        }

        try {
            let response = await API(data);
            setStatus({message: response.message, type: response.status == "OK" ? "success" : "error"})

        } catch (err){
            setStatus({message: "Server error", type: "error"})
        } finally {
            setLoading(false);
        }
    }


    return (
        <div className="App2">        
            <h1>Inicia Sesión</h1>
            <form onSubmit={handleSubmission}>
                <input name="email" type="email" />
                <input name="password" type="password"/>
                <button disabled={loading}>{loading ? "Enviando...": "Regístrate"}</button>
                
                {status && (
                    <div className={status.type}>
                        {status.message}
                    </div>
                )}
            </form>

        </div>

    )
}