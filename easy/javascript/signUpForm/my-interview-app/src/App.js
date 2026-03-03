import "./styles.css";
import { useState } from "react";
/*
Build a user Signup form in React with the following features.

1. An email and a password input
2. Email must have an "@" and the domain side must include a "."
3. Password must include
    1. at least one special character
    2. one number and be at least 8 characters
4. Submission request handling
    1. Utilze the mock API function to handle submissions
5. Basic aesthetics with pure CSS
*/

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

export default function App() {
    const [status, setStatus] = useState();
    const [loading, setLoading] = useState(false);

    async function handleSubmission(event) {
        event.preventDefault();
        setLoading(true);

        const data = Object.fromEntries(new FormData(event.target));

        const isEmailValid = data.email &&  data.email.split("@")[1].includes(".");
        const isPasswordValid = data.password && data.password.length >= 0 
        && /[0-9]/.test(data.password) 
        && /[^A-Za-z0-9]/.test(data.password);

        if(!isEmailValid) {
            setStatus({
                message: "Email is invalid:",
                type: "error"
            })
            setLoading(false);
            return;
        };

        if(!isPasswordValid) {
            setStatus({
                message: "Password is invalid",
                type: "error"
            })
            setLoading(false);
            return;
        }

        try {
            const response = await API(data);
            setStatus({
                message: response.message,
                type: response.status === "OK" ? "success" : "error"
            });
        } catch (err) {
            setStatus({ message: "Server error", type: "error" });
        } finally {
            setLoading(false);
        }
    }

return (
        <div className="App">
            <h1>Regístrate</h1>
            <form onSubmit={handleSubmission}>
                <input name="email" type="email" placeholder="Email" required />
                <input name="password" type="password" placeholder="Password" required />
                
                <button disabled={loading}>
                    {loading ? "Enviando..." : "Regístrate"}
                </button>

                {status && (
                    <div className={status.type}>
                        {status.message}
                    </div>
                )}
            </form>
        </div>
    );

}