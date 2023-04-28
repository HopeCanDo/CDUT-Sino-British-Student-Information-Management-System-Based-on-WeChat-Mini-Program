'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	let callback =[];
	const db = uniCloud.database();
	const collection = db.collection("grade"); 
	await collection.add({
		content:event.content,
		user_name:event.user_name,
		createdtime:event.createdtime,
		level:event.level,
		score:event.score
	})
	callback={
		code:1,
		msg:"success"
	}
	//return data to the client
	return callback
	
};
