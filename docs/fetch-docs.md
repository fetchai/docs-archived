<div class="md-typeset__scrollwrap">
  <div class="md-typeset__table">
    <table>
      <thead></thead>
      <tbody></tbody>
    </table>
  </div>
</div>

<script type="text/javascript">
  var theadTr = document.createElement("tr");

  [
    "Page",
    "Pageviews",
    "Unique Pageviews",
    "Avg. time on Page",
    "Entrances",
    "Bounce rate",
    "% Exit",
    "Page Value",
  ].forEach((item, index) => {
    let th = document.createElement("th");
    th.innerText = item;
    if (index === 0 || index === 1) {
      th.setAttribute("align", "left");
    } else {
      th.setAttribute("align", "right");
    }
    theadTr.appendChild(th);
  });

  document.querySelector("thead").appendChild(theadTr);

  fetch("{{fetch_docs_api}}")
    .then((response) => response.json())
    .then(({ data }) => {
      data.forEach(
        ({
          id,
          page_path,
          page_views,
          unique_page_views,
          avg_time_on_page,
          entrances,
          bounce_rate,
          exit_rate,
          page_value,
        }) => {
          let tr = document.createElement("tr");

          let tdOne = document.createElement("td");
          let tdTwo = document.createElement("td");
          let tdThree = document.createElement("td");
          let tdFour = document.createElement("td");
          let tdFive = document.createElement("td");
          let tdSix = document.createElement("td");
          let tdSeven = document.createElement("td");
          let tdEight = document.createElement("td");

          tdOne.innerText = `${id}. ${page_path}`;
          tdOne.setAttribute("align", "left");

          tdTwo.innerText = page_views;
          tdTwo.setAttribute("align", "left");

          tdThree.innerText = unique_page_views;
          tdThree.setAttribute("align", "right");

          tdFour.innerText = avg_time_on_page;
          tdFour.setAttribute("align", "right");

          tdFive.innerText = entrances;
          tdFive.setAttribute("align", "right");

          tdSix.innerText = bounce_rate;
          tdSix.setAttribute("align", "right");

          tdSeven.innerText = exit_rate;
          tdSeven.setAttribute("align", "right");

          tdEight.innerText = page_value;
          tdEight.setAttribute("align", "right");

          tr.appendChild(tdOne);
          tr.appendChild(tdTwo);
          tr.appendChild(tdThree);
          tr.appendChild(tdFour);
          tr.appendChild(tdFive);
          tr.appendChild(tdSix);
          tr.appendChild(tdSeven);
          tr.appendChild(tdEight);

          document.querySelector("tbody").appendChild(tr);
        }
      );
    })
    .catch((error) => {
      console.error(error);
    });
</script>
