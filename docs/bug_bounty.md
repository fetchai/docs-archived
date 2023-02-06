# Bug Bounty Program

The Fetch bug bounty program provides incentives for developers and security experts to report vulnerabilities in the Fetch ecosystem. 

The Fetch team has undertaken risk mitigation measures to limit the potential impacts of bugs or intentional misuse of the software and to ensure that all software has been internally audited and thoroughly tested. 

In addition to the implemented safety measures, we are offering a bug bounty for the core components of the Fetch ecosystem as outlined under the [Scope](#scope) section below. The bug bounty program ensures that the software lives up to the highest standards possible and that the risk of users losing funds is at a minimum.

## Scope

The scope of the bounty program extends to:

- FetchD: <https://github.com/fetchai/fetchd>
- Fetch Wallet: <https://github.com/fetchai/fetch-wallet>
- The Block Explorer: <https://github.com/fetchai/cosmos-explorer>
- Documentation:: <https://github.com/fetchai/docs>
- CosmPy: <https://github.com/fetchai/cosmpy>
- AEA Framework, including the ACN and packages authored by Fetchai: <https://github.com/fetchai/agents-aea> and <https://pypi.org/project/aea>
- AEA Manager Website: <https://github.com/fetchai/agents-manager-app-site>

## Classification

### Critical Bugs (awards up to 20,000 FET tokens)

Critical bugs are those that result in loss of funds or lead to a lack of availability of the network. This may be as a result of vulnerabilities found in the deployed and supported versions of the blockchain client, smart contracts or any of the other software outlined within the [Scope](#scope) section.

### Non-critical Bugs (awards up to 10,000 FET tokens)

Non-critical bugs are those that cannot cause loss of funds or any other type of economic loss. These types of bugs affect the experience of developers or users of the network and have a perceived or Fetch suggested workaround.

Awards are issued subject to reclassification and verification by the Fetch team.

## How to Report

Please follow the steps listed below to report your bug:

- In an email, describe the issue clearly with reference to the underlying source code and indicate whether the bug is **Critical** or **Non-critical**.
- Attach all relevant information that is required to reproduce the bug in a test environment.
- Include the relevant version information associated with the faulty software of the components along with any other relevant system information such as OS versions.
- Include suggested solutions and/or mitigations (if known).
- Send this email to [bounty@fetch.ai](mailto:bounty@fetch.ai) and start the subject with your classification **Critical** or **Non-critical** followed by a short title of the bug.

The Fetch team will review your information and your classification of the bug. After reviewing, one of the Fetch developers will set out to reply within 2 working days to confirm whether the bug meets the requirements of the bug bounty program or to request more time to complete this assessment. The Fetch team will also post updates on the #bugs channel on our Discord server: <https://discord.gg/M9XmgyWzup>.

For non-critical bugs, the Fetch team will create an issue or a pull request allowing you to follow the progress on the bug fix.

For critical bugs that can result in loss of funds, it is important that the Fetch team has an opportunity to deploy a patched version before the exploit is acknowledged publicly. Hence, critical bugs and their fixes will be shared after the code is patched to prevent the targeting of such exploits.

## Terms and Conditions

These include, but are not limited to:

* Bounty awards are made at the sole discretion of Fetch.ai and are subject to change and verification. 
* We will make every attempt to respond to all submissions promptly and to provide rewards in a timely manner but do not make any guarantees as to how long the processing of claims will take. 
* All users warrant that they are legally able to receive bounties. More specifically: they are of the appropriate age, the work they are submitting is their own and that they are resident in a territory that allows payment of such rewards. 
* Submitters must be willing to undergo any Know Your Customer (KYC) or Anti-Money Laundering (AML) checks as required.
* This program is not open to Fetch.ai employees or contractors, past or present. 
* Fetch.ai reserves the right to alter or discontinue the Bug Bounty Program without notice.
