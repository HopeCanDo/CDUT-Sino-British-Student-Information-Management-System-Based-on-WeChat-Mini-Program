<template>
	<view>
		<map style="width: 100vw; height: 100vh;" :latitude="latitude" :longitude="longitude" :scale="scale" :circles="circles"
			:markers="markers"></map>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				latitude: 39.909, //Set to the capital by default
				longitude: 116.39742,
				scale: 17, //Default 16
				markers: [],
				markerHeight: 30,
			};
		},
		onLoad(){
			if(!uni.getStorageSync('user_name')){
				uni.showToast({
					title:'Please login!',
					icon:'error'
				})
				uni.navigateTo({
					url:'/pages/login/login'
				})
			}
		},
		methods: {
			//Initial Location Authorization
			getAuthorize() {
				return new Promise((resolve, reject) => {
					uni.authorize({
						scope: "scope.userLocation",
						success: () => {
							resolve(); //Allow Authorization
						},
						fail: () => {
							reject(); //Deny Authorization
						},
					});
				});
			},
			//After confirming authorization, obtain user location
			getLocationInfo() {
				const that = this;
				uni.getLocation({
					type: "gcj02",
					success: function(res) {
						//Temporary
						that.longitude = res.longitude; //118.787575;
						that.latitude = res.latitude; //32.05024;
						that.markers = [{
								id: 1,
								latitude: res.latitude,
								longitude: res.longitude,
								iconPath: "../../static/position.png",
								width: that.markerHeight, //Wide
								height: that.markerHeight, //High
							},
							{
								id: 2,
								latitude: 30.674912,
								longitude: 104.147257,
								iconPath: "../../static/about.png",
								width: that.markerHeight, //Wide
								height: that.markerHeight, //High
							},
						];
						that.circles = [{ //Display circles on the map
							latitude: res.latitude,
							longitude: res.longitude,
							fillColor: "#D9E6EF", //Fill Color
							color: "#A7B6CB", //The color of the stroke
							radius:10,//radius
							strokeWidth: 2 //描边的宽度
						}]
					},
				});
			},
			//After rejecting the authorization, the pop-up prompts whether to manually open the position authorization
			openConfirm() {
				return new Promise((resolve, reject) => {
					uni.showModal({
						title: "Request authorization for current location",
						content: "We need to obtain geographic location information and recommend nearby locations for you",
						success: (res) => {
							if (res.confirm) {
								uni.openSetting().then((res) => {
									if (res[1].authSetting["scope.userLocation"] === true){
										resolve(); // Open Map Permission Settings
									} else {
										reject();
									}
								});
							} else if (res.cancel) {
								reject();
							}
						},
					});
				});
			},
			// Completely reject location acquisition
			rejectGetLocation() {
				uni.showToast({
					title: "You have refused authorization and cannot obtain surrounding information",
					icon: "none",
					duration: 2000,
				});
			},
		},
		onReady() {
			//   wx requests to obtain location permissions
			this.getAuthorize()
				.then(() => {
					//   Obtain after consent
					this.getLocationInfo();
				})
				.catch(() => {
					//   Disagree to provide the bullet box, please confirm again
					this.openConfirm()
						.then(() => {
							this.getLocationInfo();
						})
						.catch(() => {
							this.rejectGetLocation();
						});
				});
		},
	};
</script>
