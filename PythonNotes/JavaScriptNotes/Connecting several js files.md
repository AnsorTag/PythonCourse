#javaScript 

---

### **Splitting JavaScript into Two Files**

**1. HTML Setup:**

Include both JavaScript files in your HTML, ==loading the supplementary functions file before the main script:==

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bankist App</title>
</head>
<body>
  <!-- Load supplementary functions first -->
  <script src="supplementary.js"></script>
  <!-- Load main script after supplementary functions -->
  <script src="main.js"></script>
</body>
</html>
```

**2. Supplementary Functions (`supplementary.js`):**

Define utility functions here. For example:

```javascript
"use strict";

// Converts full name to initials
function usernameCreator(accounts) {
  accounts.forEach(account => {
    account.username = account.owner
      .toLowerCase()
      .split(" ")
      .map(word => word[0])
      .join("");
  });
}
```

**3. Main Script (`main.js`):**

Use the functions defined in `supplementary.js` and include your main logic:

```javascript
"use strict";

// Account info
const accounts = [ /* your account objects */ ];

// Call the supplementary function
usernameCreator(accounts);

// Element selection
const loginButton = document.querySelector(`.login`);
const inputLoginUsername = document.querySelector(`.login__input--user`);
const inputLoginPassword = document.querySelector(`.login__input--pin`);
const appContainer = document.querySelector(`.app`);
const labelWelcome = document.querySelector(`.welcome`);

let currentAccount;

loginButton.addEventListener(`click`, function (e) {
  e.preventDefault();

  currentAccount = accounts.find(
    account => account.username === inputLoginUsername.value
  );

  if (currentAccount?.pin === +inputLoginPassword.value) {
    labelWelcome.textContent = `Welcome back, ${currentAccount.owner.split(` `)[0]}`;
    appContainer.style.opacity = 100;
  }
});
```

**4. Testing and Debugging:**

- **Test**: Ensure the app functions correctly, with usernames generated and login working.
- **Debug**: Check the console for errors if issues arise, and confirm correct file loading order.

---

This summary provides a quick reference for organizing and linking JavaScript files effectively.