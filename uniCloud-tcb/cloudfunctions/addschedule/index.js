'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	let callback =[];
	const db = uniCloud.database();
	const collection = db.collection("schedule"); 
	await collection.add({
		subject:event.subject,
		user_name:event.user_name,
		teacher:event.teacher,
		classroom:event.classroom,
		day:event.day,
		time:event.time,
		Monday:event.Monday,
		Tuesday:event.Tuesday,
		Wednesday:event.Wednesday,
		Thursday:event.Thursday,
		Friday:event.Friday
	})
	callback={
		code:1,
		msg:"success"
	}
	//return data to the client
	return callback
	
};
