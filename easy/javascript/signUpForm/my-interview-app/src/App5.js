import "./styles.css";
import { useState } from "react";
/*
Build a user Signup form in React with the following features.

1. An email and a password input
2. Email must have an “@” and the domain side must include a “.”
3. Password must include
    1.  at least one special character
    2. one number and be at least 8 characters
4. Submission request handling  
   1. Utilize the mock API function to handle submissions
5. Basic aesthetics with pure CSS
*/

function API(data) {
  return new Promise((res) => {
    const isRepeated = data.email === "repeated@gmail.com";
    setTimeout(
      () =>
        res({
          status: isRepeated ? "ERROR" : "OK",
        }),
      1000
    );
  });
}

export default function App() {
  const [status, setStatus] = useState();
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    let data = Object.fromEntries(new FormData(event.target));

    let isEmailValid =
      data.email &&
      data.email.includes("@") &&
      data.email.split("@")[1].includes(".");

    let isPasswordValid =
      data.password &&
      data.password.length >= 8 &&
      /[0-9]/.test(data.password) &&
      /[A-Za-z0-9]/.test(data.password);

    if (!isEmailValid) {
      setStatus({
        type: "error",
        message: "Email is invalid",
      });
      setLoading(false);

      return;
    }

    if (!isPasswordValid) {
      setStatus({
        type: "error",
        message: "Password is invalid",
      });
      setLoading(false);

      return;
    }

    try {
      let res = await API(data);
      setStatus({
        type: res.status == "OK" ? "success" : "error",
        message:
          res.status == "OK" ? "Sign up successful!" : "Email already in use",
      });
    } catch (err) {
      setStatus({
        type: res.status == "OK" ? "success" : "error",
        message: "Server error",
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="App">
      <h1>Signup Form </h1>
      <form onSubmit={handleSubmit}>
        <input name="email" type="email" />
        <input name="password" type="password" />
        <button disabled={loading}>{loading ? "Sending..." : "Submit"}</button>
        {status && <div className={status.type}>{status.message}</div>}
      </form>
    </div>
  );
}
