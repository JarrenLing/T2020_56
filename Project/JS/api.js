var myHeaders = new Headers();

function getData() {

	var requestOptions = {
		method: 'GET',
		headers: myHeaders
	};

	return fetch("https://api.data.gov.sg/v1/transport/carpark-availability?date_time=2019-12-31T09:55:55", requestOptions)
	.then((response) => {
		if(response.ok) {
			return response.json();
		} else {
			throw new Error('Server response wasn\'t OK');
		}
	})
	.then((data) => {
		// console.log(JSON.stringify(data));
		const newvar = data.items;
		return newvar;
	})
}

var data = getData();