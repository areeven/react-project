let xhr = new XMLHttpRequest();

const getXmlHttpRequestObject = () => {
  if (!xhr) {
    // Create new XMLHttpRequest object
    xhr = new XMLHttpRequest();
  }
  return xhr;
};

const getDate = () => {
  // Implement the logic for getting the date
  const date = new Date().toString();
  const timeContainer = document.getElementById("time-container");
  if (timeContainer) {
    timeContainer.textContent = date;
  } else {
    console.log("timeContainer is null");
  }
};

const dataCallBack = () => {
  // Check response is ready or not
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log("Users received");
    getDate();
    const dataDiv = document.getElementById("result-container");
    if (dataDiv) {
      dataDiv.innerHTML = xhr.responseText;
    } else {
      console.log("dataDiv is null");
    }
  }
};

const getUsers: any = () => {
  console.log("Getting users");
  xhr = getXmlHttpRequestObject();
  xhr.onreadystatechange = dataCallBack;

  xhr.open("GET", "http://localhost:6969/users", true);
  xhr.send(null);
};

(function () {
  getDate();
})();

const Users: React.FC = () => {
  return (
    <div className="text-center">
      <h1>Users</h1>
      <div>
        <span>Last update: </span>
        <span id="time-container"></span>
      </div>
      <button
        className="bg-red-700 rounded border-solid border-2 p-2 border-black"
        onClick={getUsers}
      >
        Get User data
      </button>
      <div
        id="result-container"
        className="border-solid border-2 border-black p-2 w-1/2 mx-auto mt-4"
      ></div>
    </div>
  );
};

export default Users;
