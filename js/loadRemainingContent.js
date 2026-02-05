document.addEventListener("DOMContentLoaded", async () => {
  const url = "/index-data.json";

  try {
    const response = await makeRequest("GET", url);
    const theJSON = JSON.parse(response);
    replacePosts(theJSON);
  } catch (err) {
    console.error("Error loading posts:", err.message);
  }

  function replacePosts(theJSON) {
    const newInnerHTML = theJSON.map(p => `
            <li itemscope itemtype="http://schema.org/BlogPosting">
              <span class="post-date">${p.pretty_date || " "}</span>
              <meta itemprop="datePublished" content="${p.date || " "}" />
              <meta itemprop="dateModified" content="${p.date || " "}" />
              <span itemprop="author" itemscope itemtype="http://schema.org/Person">
                <span itemprop="name" content="${p.author || " "}"></span>
              </span>

              <span itemprop="publisher" itemscope itemtype="https://schema.org/Organization">
                <span itemprop="logo" itemscope itemtype="https://schema.org/ImageObject">
                  <meta itemprop="url" content="https://upload.wikimedia.org/wikipedia/commons/9/9e/Sus_scrofa_avionica.png">
                  <meta itemprop="width"  content="700">
                  <meta itemprop="height" content="500">
                </span>
              <meta itemprop="name" content="Notion Parallax">
              </span>

              <span itemprop="image" itemscope itemtype="https://schema.org/ImageObject">
                <meta itemprop="url" content="https://upload.wikimedia.org/wikipedia/commons/9/9e/Sus_scrofa_avionica.png">
                  <meta itemprop="width"  content="700">
                  <meta itemprop="height" content="500">
              </span>

              <h2 itemprop="headline">
                <a itemprop="mainEntityOfPage" class="post-link" href="${p.url || " "}">${p.title || " "}</a>
              </h2>

              <p itemprop="description">${p.description || ">_"}</p>
            </li>`).join('');

    const postList = document.querySelector(".post-list");
    if (postList) {
      postList.innerHTML = newInnerHTML;
      console.log("Added the extra posts");
    }
  }
});
