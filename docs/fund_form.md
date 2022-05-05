<h1>Apply for $150M Developer Fund</h1>
<div class="form-wrapper">
  <form onsubmit="onSubmitHandler(event)">
    <p>Following the announcement of the development fund for growing Fetch.ai ecosystem, we are accepting applications from prospective projects either from Cosmos or EVM to build upon Fetch.ai network or scale using Fetch.ai's toolkits.</p>
    <p>Please fill the form out if you're interested to apply for the developer grant. </p>
    <div class="group">
      <div class="form-label">
        <label>Name</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="name" name="name" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project/Company Name [If available]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectName" name="projectName" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Contact Email (if you're applying on behalf of a project or a company, please enter the email of the main point of contact)</label>
        <span class="required-mark">*</span>
      </div>
      <input type="email" id="contactEmail" name="contactEmail" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project links [Please provide Github, Website, Twitter if available]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectLinks" name="projectLinks" placeholder="Your answer" required="required"/>
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
            <input type="radio" name="category" value="dApps">
            <label>dApps</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="On-chain analytics">
            <label>On-chain analytics</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="Automation">
            <label>Automation</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="DeFi">
            <label>DeFi</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="Infrastructure">
            <label>Infrastructure</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="category" value="NFTs">
            <label>NFTs</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" id="otherRadioButton" name="category" value="Other">
            <label>Other:</label>
          </div>
          <div class="extra">
            <input type="text" id="otherCategoryFieldValue" value="" onkeypress="selectCategoryOtherRadioButton()" />
            <span class="bar"></span>
          </div>
        </label>
      </div>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project description [Please outline in detail the project you're seeking to receive a grant for]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectDescription" name="projectDescription" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Have you received any funding previously?</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="receivedFund" name="receivedFund" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Please share any details on the project tokenomics [if available]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectTokenomics" name="projectTokenomics" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>What do you want to achieve through your project?</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="achievementGoal" name="achievementGoal" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project development timelines</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectTimelines" name="projectTimelines" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Project Milestones</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="projectMilestones" name="projectMilestones" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>What is the funding amount you are looking for?</label>
      </div>
      <div class="radio-group">
        <label>
          <div class="radio">
            <input type="radio" name="projectFunding" value="50000">
            <label>Around $50,000</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="projectFunding" value="50000-150000">
            <label>Between $50,000 to $150,000</label>
          </div>
        </label>
        <label>
          <div class="radio">
            <input type="radio" name="projectFunding" value="+150000">
            <label>More than $150,000</label>
          </div>
        </label>
      </div>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Funding request breakdown [Please describe how the funds will be used]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="fundingBreakdown" name="fundingBreakdown" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <div class="form-label">
        <label>Additional attachments [Please share links - e.g dropbox/google drive]</label>
        <span class="required-mark">*</span>
      </div>
      <input type="text" id="additionalAttachments" name="additionalAttachments" placeholder="Your answer" required="required"/>
      <span class="bar"></span>
    </div>
    <div class="group">
      <button type="submit" class="btn btn-submit">Submit</button>
    </div>
  </form>
</div>

<script type="text/javascript">
  const nameInput = document.getElementById("name");
  const projectNameInput = document.getElementById("projectName");
  const contactEmailInput = document.getElementById("contactEmail");
  const projectLinksInput = document.getElementById("projectLinks");
  const projectDescriptionInput = document.getElementById("projectDescription");
  const receivedFundInput = document.getElementById("receivedFund");
  const projectTokenomicsInput = document.getElementById("projectTokenomics");
  const achievementGoalInput = document.getElementById("achievementGoal");
  const projectTimelinesInput = document.getElementById("projectTimelines");
  const projectMilestonesInput = document.getElementById("projectMilestones");
  const fundingBreakdownInput = document.getElementById("fundingBreakdown");
  const additionalAttachmentsInput = document.getElementById("additionalAttachments");

const onSubmitHandler = (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const formProps = Object.fromEntries(formData);

  let categoryValue = ""


  if(formProps.category === "Other"){
    categoryValue = document.getElementById("otherCategoryFieldValue").value;
  } else {
    categoryValue = formProps.category
  }

  console.log({...formProps, category: categoryValue})

fetch('http://localhost:7105/api/docs', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({...formProps, category: categoryValue}),
})
.then((response) => response.json())
.then((data) => {
  alert(data.message)
  resetInputValues()
})
.catch((error) => {
  alert(JSON.stringify(error))
  console.error('Error:', error);
});

}

function resetInputValues () {
  nameInput.value = ""
  projectNameInput.value = ""
  contactEmailInput.value = ""
  projectLinksInput.value = ""
  projectDescriptionInput.value = ""
  receivedFundInput.value = ""
  projectTokenomicsInput.value = ""
  achievementGoalInput.value = ""
  projectTimelinesInput.value = ""
  projectMilestonesInput.value = ""
  fundingBreakdownInput.value = ""
  additionalAttachmentsInput.value = ""
  document.querySelector('input[name="projectFunding"]:checked').checked = false;
  document.querySelector('input[name="category"]:checked').checked = false;
  document.getElementById("otherCategoryFieldValue").value = ""
}

function selectCategoryOtherRadioButton() {
 document.getElementById("otherRadioButton").checked = true;
}
</script>
