data = [
  {
    title: "Web Design And Development",
    top_header: "deom",
    content_header_1: "djajaj",
    content_header_2: "jdjsjs",
    content_header_3: "jajajajja",
    content_header_4: "jjjjj",
    content_text_1: "text1",
    content_text_2: "text2",
    content_text_3: "text3",
    content_text_4: "text4"
  }
];

async function addProducts() {
  for (const service of data) {
    try {
      const response = await fetch("http://127.0.0.1:8000/run_script/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(service)
      });
      if (response.ok) {
        console.log(`Successfully added service ${service.title}`);
      } else {
        console.error(`Failed to add service: ${service.title}`);
      }
    } catch (error) {
      console.error("Error adding product:", error);
    }
  }
}

addProducts();
