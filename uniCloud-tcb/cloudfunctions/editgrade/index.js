'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection = await db.collection("grade");

	let res = await collection.where({
		_id: event.grade_id
	}).update({
		content: event.grade_content,
		level: event.grade_level,
		score: event.grade_score
	})
	//return data to the client
	return res
};