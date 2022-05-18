<h1>Apply for $150M Developer Fund</h1>
<div class="form-wrapper">
  <form onsubmit="onSubmitHandler(event)">
    <p>
      Following the announcement of the development fund for growing Fetch.ai
      ecosystem, we are accepting applications from prospective projects either
      from Cosmos or EVM to build upon Fetch.ai network or scale using
      Fetch.ai's toolkits.
    </p>
    <p>
      Please fill the form out if you're interested to apply for the developer
      grant.
    </p>
    <div class="group">
      <div class="form-label">
        <label>Name</label>
        <span class="required-mark">*</span>
      </div>
      <input
        type="text"
        id="name"
        name="name"
        placeholder="Your answer"
        required="required"
      />
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project/Company Name [If available]</label>
        <span class="required-mark">*</span>
      </div>
      <input
        type="text"
        id="projectName"
        name="projectName"
        placeholder="Your answer"
        required="required"
      />
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Contact Email (if you're applying on behalf of a project or a
          company, please enter the email of the main point of contact)</label
        >
        <span class="required-mark">*</span>
      </div>
      <input
        type="email"
        id="contactEmail"
        name="contactEmail"
        placeholder="Your answer"
        required="required"
      />
      <span class="bar"></span>
      <span id="emailError"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Project links [Please provide Github, Website, Twitter if
          available]</label
        >
        <span class="required-mark">*</span>
      </div>
      <input
        type="text"
        id="projectLinks"
        name="projectLinks"
        placeholder="Your answer"
        required="required"
      />
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Which category does your project fall under?</label>
        <span class="required-mark">*</span>
      </div>
      <div class="radio-group">
        <label>
          <div class="radio">
            <input type="radio" name="category" value="dApps" id="dApps" />
            <label for="dApps">dApps</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="category"
              value="On-chain analytics"
              id="analytics"
            />
            <label for="analytics">On-chain analytics</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="category"
              value="Automation"
              id="automation"
            />
            <label for="automation">Automation</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="DeFi" id="DeFi" />
            <label for="DeFi">DeFi</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="category"
              value="Infrastructure"
              id="infrastructure"
            />
            <label for="infrastructure">Infrastructure</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="NFTs" id="nfts" />
            <label for="nfts">NFTs</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              id="otherRadioButton"
              name="category"
              value="Other"
            />
            <label for="otherRadioButton">Other:</label>
          </div>
          <div class="extra">
            <input
              type="text"
              id="otherCategoryFieldValue"
              value=""
              onkeypress="selectCategoryOtherRadioButton()"
            />
            <span class="bar"></span>
          </div>
        </label>
      </div>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Project description [Please outline in detail the project you're
          seeking to receive a grant for]</label
        >
        <span class="required-mark">*</span>
      </div>
      <textarea
        id="projectDescription"
        name="projectDescription"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Have you received any funding previously?</label>
        <span class="required-mark">*</span>
      </div>
      <div class="radio-group">
        <label>
          <div class="radio">
            <input
              type="radio"
              id="receivedFundOne"
              name="receivedFund"
              value="Yes [provide the source(s)]"
            />
            <label for="receivedFundOne">Yes:</label>
          </div>
          <div class="extra">
            <input
              type="text"
              id="receivedFundOneFieldValue"
              value=""
              onkeypress="selectReceivedFundOneRadioButton()"
            />
            <span class="bar"></span>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="receivedFund"
              value="No"
              id="receivedFundTwo"
            />
            <label for="receivedFundTwo">No</label>
          </div>
        </label>
      </div>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Please share any details on the project tokenomics [if
          available]</label
        >
        <span class="required-mark">*</span>
      </div>
      <textarea
        id="projectTokenomics"
        name="projectTokenomics"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>What do you want to achieve through your project?</label>
        <span class="required-mark">*</span>
      </div>
      <textarea
        type="text"
        id="achievementGoal"
        name="achievementGoal"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project development timelines</label>
        <span class="required-mark">*</span>
      </div>
      <textarea
        type="text"
        id="projectTimelines"
        name="projectTimelines"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project Milestones</label>
        <span class="required-mark">*</span>
      </div>
      <textarea
        type="text"
        id="projectMilestones"
        name="projectMilestones"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>What is the funding amount you are looking for?</label>
      </div>
      <div class="radio-group">
        <label>
          <div class="radio">
            <input
              type="radio"
              name="projectFunding"
              value="50000"
              id="projectFunding1"
            />
            <label for="projectFunding1">Less than $50,000</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="projectFunding"
              value="50000-150000"
              id="projectFunding2"
            />
            <label for="projectFunding2">Between $50,000 to $150,000</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input
              type="radio"
              name="projectFunding"
              value="+150000"
              id="projectFunding3"
            />
            <label for="projectFunding3">More than $150,000</label>
          </div>
        </label>
      </div>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Funding request breakdown [Please describe how the funds will be
          used]</label
        >
        <span class="required-mark">*</span>
      </div>
      <textarea
        type="text"
        id="fundingBreakdown"
        name="fundingBreakdown"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label
          >Additional attachments [Please share links - e.g dropbox/google
          drive]</label
        >
        <span class="required-mark">*</span>
      </div>
      <textarea
        type="text"
        id="additionalAttachments"
        name="additionalAttachments"
        placeholder="Your answer"
        required="required"
        cols="5"
        rows="5"
      ></textarea>
      <span class="bar"></span>
    </div>
    <div class="group">
      <button type="submit" id="submit_btn" class="btn btn-submit">
        Submit
      </button>
    </div>
  </form>
  <!-- The snackbar -->
  <div id="snackbar">
    <div id="snackbar_text"></div>
  </div>
</div>

<script type="text/javascript">
  const nameInput = document.getElementById("name");
  const projectNameInput = document.getElementById("projectName");
  const contactEmailInput = document.getElementById("contactEmail");
  const projectLinksInput = document.getElementById("projectLinks");
  const projectDescriptionInput = document.getElementById("projectDescription");
  const projectTokenomicsInput = document.getElementById("projectTokenomics");
  const achievementGoalInput = document.getElementById("achievementGoal");
  const projectTimelinesInput = document.getElementById("projectTimelines");
  const projectMilestonesInput = document.getElementById("projectMilestones");
  const fundingBreakdownInput = document.getElementById("fundingBreakdown");
  const additionalAttachmentsInput = document.getElementById(
    "additionalAttachments"
  );
  const emailErrorField = document.getElementById("emailError");
  const submitButton = document.getElementById("submit_btn");
  const submitButtonText = submitButton.innerText;

  const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
  };

  const onSubmitHandler = (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const formProps = Object.fromEntries(formData);
    let categoryValue = "";
    let receivedFundValue = "";

    if (formProps.category === "Other") {
      categoryValue = document.getElementById("otherCategoryFieldValue").value;
    } else {
      categoryValue = formProps.category;
    }

    if (formProps.receivedFund === "Yes") {
      receivedFundValue = document.getElementById(
        "receivedFundOneFieldValue"
      ).value;
    } else {
      receivedFundValue = formProps.receivedFund;
    }

    if (formProps.contactEmail.trim() === "") {
      emailErrorField.innerText = "Email address is required";
      return;
    } else {
      emailErrorField.innerText = "";
    }

    if (!validateEmail(formProps.contactEmail)) {
      emailErrorField.innerText = "Please enter a valid email address";
      return;
    } else {
      emailErrorField.innerText = "";
    }

  
    submitButton.disabled = true;
    submitButton.innerHTML = `<svg class="spinner" viewBox="0 0 25 25">
  <circle class="path" cx="12.5" cy="12.5" r="10" fill="none" stroke-width="2"></circle>
</svg>`;

    fetch("{{fund_form_api}}/api/docs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...formProps,
        category: categoryValue,
        receivedFund: receivedFundValue,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        showSnackBar(data.message);
        submitButton.removeAttribute("disabled");
        submitButton.innerHTML = submitButtonText;
        resetInputValues();
      })
      .catch((error) => {
        showSnackBar("Something went wrong! Please try again later", "danger");
        submitButton.removeAttribute("disabled");
        submitButton.innerHTML = submitButtonText;
        console.error("Error:", error);
      });
  };

  function resetInputValues() {
    nameInput.value = "";
    projectNameInput.value = "";
    contactEmailInput.value = "";
    projectLinksInput.value = "";
    projectDescriptionInput.value = "";
     document.querySelector(
      'input[name="receivedFund"]:checked'
    ).checked = false;
    document.getElementById("receivedFundOneFieldValue").value = "";
    projectTokenomicsInput.value = "";
    achievementGoalInput.value = "";
    projectTimelinesInput.value = "";
    projectMilestonesInput.value = "";
    fundingBreakdownInput.value = "";
    additionalAttachmentsInput.value = "";
    document.querySelector(
      'input[name="projectFunding"]:checked'
    ).checked = false;
    document.querySelector('input[name="category"]:checked').checked = false;
    document.getElementById("otherCategoryFieldValue").value = "";
  }

  function selectCategoryOtherRadioButton() {
    document.getElementById("otherRadioButton").checked = true;
  }

  function selectReceivedFundOneRadioButton() {
    document.getElementById("receivedFundOne").checked = true;
  }

  function showSnackBar(text = "", variant = "normal") {
    const snackbarDiv = document.getElementById("snackbar");
    const snackbarText = document.getElementById("snackbar_text");

    snackbarText.innerHTML = text;

    // Add the "show" class to DIV
    snackbarDiv.className = "snackbar__show";

    if (variant === "danger") {
      snackbarDiv.className += " snackbar__danger";
    }

    // After 3 seconds, remove the class names from DIV
    setTimeout(function () {
      snackbarDiv.className = "";
    }, 3000);
  }
</script>
