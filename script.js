async function sendQuery() {
      const queryInput = document.getElementById("query");
      const query = queryInput.value.trim();
      const responseDiv = document.getElementById("response");

      if (!query) {
        alert("Please enter a query.");
        return;
      }

      responseDiv.innerHTML = "Loading...";

      try {
        const res = await fetch(`http://localhost:8003/assistant?message=${encodeURIComponent(query)}`);
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await res.json();

        // Deconstruct potential fields from the assistant response
        const { price, news, alert, response: fallback } = data.response;

        let displayText = "";

        if (price && price.BTC) {
          displayText += `Current BTC Price: ${price.BTC}\n\n`;
        }

        if (news && news.headlines) {
          displayText += `Top Headlines:\n  - ${news.headlines.join("\n  - ")}\n\n`;
        }

        if (alert && alert.alert) {
          displayText += `Alert: ${alert.alert}\n\n`;
        }

        if (!displayText && fallback) {
          displayText = fallback;
        }

        responseDiv.innerHTML = displayText;
      } catch (error) {
        responseDiv.innerHTML = `Error: ${error.message}`;
      }
    }