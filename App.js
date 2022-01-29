import { StatusBar } from 'expo-status-bar';
import { View, Text, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import {
  createDrawerNavigator,
  DrawerContentScrollView,
  DrawerItemList,
  DrawerItem,
} from '@react-navigation/drawer';

import Dashboard  from "./src/screens/Dashboard"
import LoginScreen from './src/screens/LoginScreen'
import StartScreen from './src/screens/StartScreen';
import RegisterScreen from './src/screens/RegisterScreen';
import DrawerNavigatorRoutes from './src/screens/DrawerNavigationRoutes';

function Feed({ navigation }) {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Feed Screen</Text>
      <Button title="Open drawer" onPress={() => navigation.openDrawer()} />
      <Button title="Toggle drawer" onPress={() => navigation.toggleDrawer()} />
    </View>
  );
}

function Notifications() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Notifications Screen</Text>
    </View>
  );
}

function CustomDrawerContent(props) {
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <DrawerItem
        label="Close drawer"
        onPress={() => props.navigation.closeDrawer()}
      />
      <DrawerItem
        label="Toggle drawer"
        onPress={() => props.navigation.toggleDrawer()}
      />
    </DrawerContentScrollView>
  );
}

const Drawer = createDrawerNavigator();

function MyDrawer() {
  return (
    <Drawer.Navigator>
      <Drawer.Screen name="DIB e.V"  component={StartScreen}
      options={{drawerLabel: 'DIB e.V y', title: 'DIV e.V e'}} />
      <Drawer.Screen name="LoginScreen" component={LoginScreen} />
      <Drawer.Screen name="RegisterScreen" title="Register" component={RegisterScreen} />
      <Drawer.Screen  name="DrawerNavigatorRoutes" title="User Dashboard" component={DrawerNavigatorRoutes}
      options={{headerShown: false}} />
    </Drawer.Navigator>

  );
}

export default function App() {
  return (
    <NavigationContainer>
      <MyDrawer />
    </NavigationContainer>
  );
}
