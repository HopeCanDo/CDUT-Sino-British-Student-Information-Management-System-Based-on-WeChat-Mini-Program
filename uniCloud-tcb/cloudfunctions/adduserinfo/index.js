'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	let callback =[];
	const db = uniCloud.database();
	const collection = db.collection("userinfo"); 
	await collection.add({
		user_name:event.user_name
	})
	callback={
		code:1,
		msg:"success"
	}
	//return data to the client
	return event
};
