import {
  Create,
  Box,
  TextField,
  FormControl,
  FormLabel,
  MenuItem,
  Select,
} from "@pankod/refine-mui";
import { useForm } from "@pankod/refine-react-hook-form";

import * as Yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";

const schema = Yup.object({
  firstName: Yup.string().required("This field is required"),
  lastName: Yup.string().required("This field is required"),
  phone: Yup.string().required("This field is required"),
});

interface formDataType {
  firstName: string;
  lastName: string;
  phone: string;
}

export const HousekeeperCreate = () => {
  const {
    saveButtonProps,
    refineCore: { formLoading },
    register,
    formState: { errors },
  } = useForm<formDataType>({ resolver: yupResolver(schema) });

  return (
    <Create isLoading={formLoading} saveButtonProps={saveButtonProps}>
      <Box
        component="form"
        sx={{ display: "flex", flexDirection: "column" }}
        autoComplete="off"
      >
        <TextField
          {...register("firstName", {
            required: "This field is required",
          })}
          required
          error={!!(errors as any)?.name}
          helperText={(errors as any)?.name?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="First Name"
          name="firstName"
        />

        <TextField
          {...register("lastName")}
          error={!!(errors as any)?.backtest_end_at}
          helperText={(errors as any)?.backtest_end_at?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="Last Name"
          name="lastName"
        />

        <TextField
          {...register("phone")}
          error={!!(errors as any)?.backtest_end_at}
          helperText={(errors as any)?.backtest_end_at?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="phone"
          name="phone"
        />
      </Box>
    </Create>
  );
};
