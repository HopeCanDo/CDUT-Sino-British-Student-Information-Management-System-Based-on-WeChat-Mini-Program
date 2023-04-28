'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection = await db.collection("schedule");

	let res = await collection.where({
		_id: event.schedule_id
	}).update({
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
	//return data to the client
	return res
};