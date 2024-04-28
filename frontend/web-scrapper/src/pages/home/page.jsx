import { Box, TextField } from "@mui/material";
import "./page.css";
import { useEffect, useState } from "react";
import EastIcon from "@mui/icons-material/East";
import axios from "axios";

function Home() {
  const [typedText, setTypedText] = useState("");
  const [fullText, setFullText] = useState("   Hello !     ");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [url, setUrl] = useState("");

  const [finish, setFinish] = useState(false);

  function nextclick() {
    console.log("clicked", name, url, email);
    if (fullText == "Enter Your Name") {
      setFinish(false);
      setTypedText("");
      setFullText("Enter Your Email");
    }
    if (fullText == "Enter Your Email") {
      setFinish(false);
      setTypedText("");
      setFullText(`Enter the Product Url`);
    }

    if (fullText == "Enter the Product Url") {
      setFinish(false);
      setTypedText("");
      setFullText(`Thanks ${name}. You will get Notification when price drops`);
    }
      if (name && url && email) {
        console.log('came to axios')
      axios.post("", {
        user: name,
        email: email,
        url: url,
      });
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (typedText.length < fullText.length) {
        setTypedText(fullText.substring(0, typedText.length + 1));
      } else if (fullText.trim() == "Hello !") {
        setTimeout(() => {
          setFullText("Welcome to Amazon Price Email Notifier");
          setTypedText(""); // Reset typedText to start typing the new message
        }, 100);
      } else if (fullText == "Welcome to Amazon Price Email Notifier") {
        setTimeout(() => {
          setFullText("Enter Your Name");
          setTypedText("");
        }, 800);
      } else if (
        fullText == "Enter Your Name" &&
        typedText === "Enter Your Name"
      ) {
        setFinish(true);
      } else if (
        fullText == "Enter Your Email" &&
        typedText === "Enter Your Email"
      ) {
        setFinish(true);
      } else if (
        fullText == "Enter the Product Url" &&
        typedText === "Enter the Product Url"
      ) {
        setFinish(true);
      }
    }, 150); // Adjust typing speed by changing delay here

    return () => {
      clearTimeout(timeoutId);
    };
  }, [typedText, fullText]);
  return (
    <>
      <Box className="rainbow-spiral">
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            textAlign: "center",
            height: "100vh",
          }}
        >
          <Box
            sx={{
              fontFamily: "roboto",
              fontSize: "34px",
              fontWeight: "600",
              color: "white",
              maxWidth: "35%",
            }}
          >
            {typedText}
          </Box>
          {finish && (
            <Box
              sx={{
                fisplay: "flex",
                flexDirection: "row",
              }}
            >
              <TextField
                sx={{
                  marginTop: "20px",
                  borderLeft: "transparent",
                  borderTop: "transparent",
                  borderRight: "transparent",
                  color: "white",
                }}
                onChange={(event) => {
                  if (fullText == "Enter Your Name") {
                    setName(event.target.value);
                  } else if (fullText == "Enter Your Email") {
                    setEmail(event.target.value);
                  } else if (fullText == "Enter the Product Url") {
                    setUrl(event.target.value);
                  }
                }}
              ></TextField>
              <div style={{ cursor: "pointer" }} onClick={() => nextclick()}>
                <EastIcon
                  sx={{
                    marginTop: "14%",
                  }}
                />
              </div>
            </Box>
          )}
        </Box>
      </Box>
    </>
  );
}

export default Home;
