import React from "react";

import colors from "../config/colors";

import GridSettings from "./GridSettings";
import ConnectionArea from "./ConnectionArea";
import IconButtonSettings from "./IconButtonSettings";

export default function SideBar(props) {
	return (
		<div style={styles.container}>
			{props.className ? 
				<IconButtonSettings
					className={props.className}
					id={props.id}
					onClick={props.onExitClick}
				/>
				:
				<ConnectionArea
				/>
			}
			<GridSettings
				numOfRows={props.numOfRows}
				numOfCols={props.numOfCols}
				numOfPages={props.numOfPages}
				onClick={(type, val) => {props.onGridSettingsClick(type, val)}}
			/>
		</div>
	);
}

const styles = {
	container: {
		flex: 1,
		display: "flex",
		flexDirection: "column",
		backgroundColor: colors.primary,
	},
};