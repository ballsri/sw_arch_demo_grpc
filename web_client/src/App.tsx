import {
  notificationProvider,
  RefineSnackbarProvider,
  CssBaseline,
  GlobalStyles,
  Layout,
  ThemeProvider,
  LightTheme,
  ReadyPage,
  ErrorComponent,
} from "@pankod/refine-mui";

import routerProvider from "@pankod/refine-react-router-v6";
import { MuiInferencer } from "@pankod/refine-inferencer/mui";
import authProvider from "authProvider";
import dataProvider from "dataProvider";
import { Refine } from "@pankod/refine-core";
import { AuthPage } from "components/pages/auth";
import {
  HousekeeperList,
  HousekeeperCreate,
  HousekeeperEdit,
} from "pages/housekeeper";
import { REST_PUBLIC_URI } from "environment";


function App() {
  return (
    <ThemeProvider theme={LightTheme}>
      <CssBaseline />
      <GlobalStyles styles={{ html: { WebkitFontSmoothing: "auto" } }} />
      <RefineSnackbarProvider>
        <Refine
          dataProvider={dataProvider(`${REST_PUBLIC_URI}/api/v1`)}
          routerProvider={{
            ...routerProvider,
            routes: [
              { path: "/", element: <AuthPage type="login" /> },
            ],
          }}
          notificationProvider={notificationProvider}
          Layout={Layout}
          ReadyPage={ReadyPage}
          catchAll={<ErrorComponent />}
          resources={[
            {
              name: "house-keepers",
              list: HousekeeperList,
              show: MuiInferencer,
              create: HousekeeperCreate,
              edit: HousekeeperEdit,
              canDelete: true,
            },
          ]}
        />
      </RefineSnackbarProvider>
    </ThemeProvider>
  );
}

export default App;
